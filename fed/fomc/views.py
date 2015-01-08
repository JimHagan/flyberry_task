import json
from django.shortcuts import render
from django.http import HttpResponse

API_VERSION = 1.0

def JsonResponse(response):
    return HttpResponse(json.dumps(response), content_type='application/json')

def version(request):
    api_info = {"description": "Federal Reserve Information API",
                "version": API_VERSION,
                "author": "Jim Hagan",
                "last_revised": "January 7, 2015"}
                
    return JsonResponse(api_info)
