from django.db import models

class MeetingScheduleEntry(models.Model):
    meeting_start_date = models.DateTimeField()
    meeting_end_date = models.DateTimeField()
    statement = models.BooleanField(default=False)
    projecttions = models.BooleanField(default=False)
    data_retrieval_date = models.DateTimeField()
    estimated_release = models.DateTimeField()
    

class MeetingTableSummary(models.Model):
    title = models.CharField(max_length=100)
    table_as_json = models.TextField()
    data_retrieval_date = models.DateTimeField()
    meeting = models.ForeignKey(MeetingScheduleEntry)
