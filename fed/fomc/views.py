import json
from django.shortcuts import render
from django.http import HttpResponse
API_VERSION = 1.0

def JsonResponse(response):
    return HttpResponse(json.dumps(response), content_type='application/json')

def version(request):
    api_info = {"status": "ok",
                "version": API_VERSION,
                "data": {"author": "Jim Hagan",
                         "last revised": "January 7, 2015",
                         "description": "Federal Reserve Information API",
                         "source repository": "https://github.com/JimHagan/flyberry_task.git"}}
                
    return JsonResponse(api_info)
