import json
from django.shortcuts import render
from django.http import HttpResponse
API_VERSION = "1.0"

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
    return successful_response(data)