from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the commissions index.")

def commissions_list(request):
    return HttpResponse("You're looking at the list of commissions.")

def commissions_detail_1(request):
    return HttpResponse("You're looking at commission detail 1.")