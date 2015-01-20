import json
import time
from datetime import datetime
from django.db import models

def _timestamp_from_datetime(dt):
    return time.mktime(dt.timetuple()) * 1000


class MeetingScheduleEntry(models.Model):
    meeting_year = models.IntegerField(null=True)
    meeting_month = models.CharField(null=True, max_length=20)
    meeting_name = models.CharField(null=True, max_length=100)
    meeting_start_date = models.DateTimeField(null=True)
    meeting_end_date = models.DateTimeField(null=True)
    statement = models.BooleanField(default=False)
    statement_url = models.CharField(null=True, max_length=256)
    projections = models.BooleanField(default=False)
    projections_pdf_url = models.CharField(null=True, max_length=256)
    projections_html_url = models.CharField(null=True, max_length=256)
    scrape_date = models.DateTimeField(null=True)
    estimated_release = models.DateTimeField(null=True)
    raw_entry = models.TextField(null=True)
    unscheduled = models.BooleanField(default=False)
    #Not as robust as possible but covers most use cases
    class Meta:
        unique_together = ("meeting_name", "scrape_date")

    def as_dict(self, columns = []):
        output_dict = {}
        _output_columns = ["id"]
        output_columns = ["id","meeting_name", "meeting_year", "meeting_month",
                        "unscheduled", "meeting_start_date",
                        "meeting_end_date", "scrape_date",
                        "statement", "statement_url", "projections","projections_pdf_url", "projections_html_url",
                        "estimated_release"] if not len(columns) else ["id"] + columns
        for column in output_columns:
            output_dict[column] = _timestamp_from_datetime(getattr(self, column)) if "date" in column or "estimated_release" in column else str(getattr(self, column))
        return output_dict
    
           
    def from_original_dict(self, meeting_dict):        
        self.meeting_month = meeting_dict["month"]
        self.meeting_year = meeting_dict["year"]
        if "statement_url" in meeting_dict:
            self.statement_url = meeting_dict["statement_url"]
            self.statement=True
        if "projections_pdf_url" in meeting_dict or "projections_html_url" in meeting_dict:
            self.projections_pdf_url = meeting_dict.get("projections_pdf_url", None)
            self.projections_html_url = meeting_dict.get("projections_html_url", None)
            self.projections = True
        self.meeting_name = ("FOMC_%s_%s" % (self.meeting_year, meeting_dict["month"])).upper()
        self.raw_entry = json.dumps(meeting_dict)
        self.scrape_date = datetime.strptime(meeting_dict["scrape_date"], "%Y-%m-%d %H:%M:%S.%f")
        timezone_offset = 5 # a kludge
        raw_days = meeting_dict["day"]
        if "unscheduled" in raw_days.lower():
            self.unscheduled=True
            self.meeting_name = self.meeting_name + "_ADHOC"
        month_num = datetime.strptime(meeting_dict["month"][:3], "%b").month
    
        days = raw_days.replace("*","").strip().split("-")
        if len(days) == 2:
            d1 = int(days[0])
            d2 = int(days[1])
         
            self.meeting_start_date = datetime(meeting_dict["year"], month_num, d1)
            self.meeting_end_date = datetime(meeting_dict["year"], month_num, d2)
            self.estimated_release = datetime(meeting_dict["year"], month_num, d2, 2 + timezone_offset)
        
        else:
            days = raw_days.replace("*","").strip().split(" ")
            if len(days):
                d1 = int(days[0])
                d2 = int(days[0])
                self.meeting_start_date = datetime(meeting_dict["year"], month_num, d1)
                self.meeting_end_date = datetime(meeting_dict["year"], month_num, d2)
                self.estimated_release = datetime(meeting_dict["year"], month_num, d2, 2 + timezone_offset)
    

    def __str__(self):
        return "%s %s %s projections=%s statement=%s" % (self.meeting_name, self.meeting_start_date, self.meeting_end_date, self.projections, self.statement)



class ProjectionTableSummary(models.Model):
    table_name = models.CharField(max_length=100)
    table_body_as_json = models.TextField()
    scrape_date = models.DateTimeField()
    meeting_schedule_entry = models.ForeignKey(MeetingScheduleEntry)
  
    def __str__(self):
        return "%s %s %s\n%s" % (self.table_name, self.scrape_date, self.meeting_schedule_entry.meeting_name, self.table_body_as_json)


    def as_dict(self):
        output_dict = {}
        _output_columns = ["m"]
        output_columns = ["table_name", "scrape_date"]
        for column in output_columns:
            output_dict[column] = _timestamp_from_datetime(getattr(self, column)) if "date" in column else str(getattr(self, column))
        output_dict["meeting_entry_id"] = self.meeting_schedule_entry_id
        output_dict["meeting_name"] = self.meeting_schedule_entry.meeting_name
        output_dict["table_body"] = json.loads(self.table_body_as_json)
        return output_dict

def populate_projection_tables(meeting_schedule_entry, projection_tables_json_list):
    if meeting_schedule_entry.projections and meeting_schedule_entry.projections_html_url and projection_tables_json_list:
        for proj_table in projection_tables_json_list:
            proj_object = ProjectionTableSummary()
            proj_object.scrape_date = meeting_schedule_entry.scrape_date
            #proj_object.units = proj_table["units"]
            proj_object.table_name = proj_table["name"]
            proj_object.table_body_as_json = json.dumps(proj_table)
            proj_object.meeting_schedule_entry = meeting_schedule_entry
            proj_object.save()
 

