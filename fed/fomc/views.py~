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
    return successful_response(json.dumps(data))


def calendar(request):
    # TODO: If there were more time, I'd create a data_pull class which would 
    # encapsulate a complete run of the data. Thereore I'd save every object we ever pull, but
    # have the notion of the most recent.  In this case if the last retrieval date is older than
    # a certain number of days, we'll just blow away th old data and re-pull.
    refresh_needed = False
    recent_recs = MeetingScheduleEntry.objects.filter(data_retrieval_date__gte=datetime.utcnow() - timedelta(days=AGE_LIMIT_DAYS))
    refresh_needed = not recent_recs.exists()
    
    if refresh_needed:
        MeetingTableSummary.objects.all().delete()
        MeetingScheduleEntry.objects.all().delete()
        raw_schedules = site_scraper.get_latest_fed_schedule()
        for sch in raw_schedules:
            print sch
            schedule_object = MeetingScheduleEntry()
            schedule_object.from_original_dict(sch)
            schedule_object.save()
            #print schedule_object.as_dict()
    
    all_objects = MeetingScheduleEntry.objects.all()
    print all_objects
    processed_objects = [obj.as_dict() for obj in all_objects]
    return successful_response(processed_objects)