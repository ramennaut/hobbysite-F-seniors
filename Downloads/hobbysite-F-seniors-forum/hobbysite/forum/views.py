from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the forum index.")

def forum_threads(request):
    return HttpResponse("You're looking at the list of forum threads.")

def forum_thread_1(request):
    return HttpResponse("You're looking at forum thread 1.")