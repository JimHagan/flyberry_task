import json
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse
from fomc import site_scraper
from fomc.models import MeetingScheduleEntry, MeetingTableSummary

API_VERSION = "1.0"
AGE_LIMIT_DAYS = 7 # abitrary

def JsonResponse(response, status=200):
    return HttpResponse(json.dumps(response), content_type='application/json', status=status)

def successful_response(data):
    result = {"status": "ok",
            "version": API_VERSION,
            "data": data}
    return JsonResponse(result, 200)
                         
def failure_response(code="00000", message="Unknown Error", http_status=500):
    result = {"status": "error",
              "code": code,
              "message": message}
    return JsonResponse(result, http_status)
            

def error404(request):
    return failure_response("404", "404 Error")

def error500(request):
    return failure_response("500", "500 Error")


def version(request):
    data = {"author": "Jim Hagan",
            "last revised": "January 7, 2015",
            "description": "Federal Reserve Information API",
            "source repository": "https://github.com/JimHagan/flyberry_task.git"}
    data_style = request.GET.get("data_style", "string")
    if data_style.lower() == "json":
        return successful_response(data)
    else:
        return successful_response(json.dumps(data))


"""
This is the primary method for querying FOMC ("Federal Reserve Open Market Committee")
meeting information.

base URL...

<server>/fed/fomc/calendar  

By itself the base URL will return a JSON repsonse with a data element containing a stringified JSON
list of meeting descriptions

Header info (successful response)...

{"status": "ok", "version": "1.0", "data": [<stringfied list of elements>]}

Example of a meeting element...

{"meeting_year": "2014", "meeting_end_date": "2014-01-29 00:00:00+00:00", "data_retrieval_date": "2015-01-08 19:44:04.281746+00:00", "meeting_start_date": "2014-01-28 00:00:00+00:00", "projections": "False", "statement": "False", "meeting_name": "FOMC_2014_JANUARY", "estimated_release": "2014-01-29 07:00:00+00:00"}

Example of an error return value...

{"status": "error", "message": "404 Error", "code": "404"} 

Supported Query Params

1. meeting_start_date_range=<dt1>, <dt2>
2.

"""
def calendar(request):
    # TODO: If there were more time, I'd create a data_pull class which would 
    # encapsulate a complete run of the data. Thereore I'd save every object we ever pull, but
    # have the notion of the most recent.  In this case if the last retrieval date is older than
    # a certain number of days, we'll just blow away th old data and re-pull.
    refresh_needed = True
    recent_recs = MeetingScheduleEntry.objects.filter(data_retrieval_date__gte=datetime.utcnow() - timedelta(days=AGE_LIMIT_DAYS))
    refresh_needed = not recent_recs.exists()
    
    if refresh_needed:
        MeetingTableSummary.objects.all().delete()
        MeetingScheduleEntry.objects.all().delete()
        print "Getting schedules..."
        raw_schedules = site_scraper.get_latest_fed_schedule()
        for sch in raw_schedules:
            if "month" in sch:
                schedule_object = MeetingScheduleEntry()
                schedule_object.from_original_dict(sch)
                schedule_object.save()
        print "Got schedules..."
        
    all_objects = MeetingScheduleEntry.objects.all().order_by("-meeting_start_date")
    #processed_objects = [obj.as_dict() for obj in all_objects]
    transposed_dict = {}
    for obj in all_objects:
        obj_dict = obj.as_dict()
        _ID = obj_dict["meeting_name"]
        for k, v in obj_dict.items():
            if not k in transposed_dict:
                transposed_dict[k] = {_ID: v}
            else:
                transposed_dict[k][_ID] = v
            
    
    data_style = request.GET.get("data_style", "string")
    if data_style.lower() == "json":
        return successful_response(transposed_dict)
    else:
        return successful_response(json.dumps(transposed_dict))