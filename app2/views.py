from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vani(request):
    return HttpResponse('<marquee>very talanted girl</marquee>')
def mamatha(request):
    return HttpResponse('<i>friendly nature</i>')