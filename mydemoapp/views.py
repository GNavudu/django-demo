from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import admin

def greeting_service(request):
    return HttpResponse("Hello, world!")

    return HttpResponse("Hello, world!")