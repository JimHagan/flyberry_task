from django.shortcuts import render_to_response
from django.http import HttpResponse

def index_page(request):
    return render_to_response('index.html')
    