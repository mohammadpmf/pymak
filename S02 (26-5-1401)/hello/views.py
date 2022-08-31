from django.shortcuts import render
from django.http import HttpResponse

def show_hello(request):
    return HttpResponse("Hello World")

def show_amir(request):
    return HttpResponse("Hello Amir")