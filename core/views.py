from django.shortcuts import render
from django.http import HttpResponse
from dockerlearn505._celery import add
# Create your views here.

def home_page(request):
    add.delay(50, 20)
    return HttpResponse('Learning docker, Celery, Redis, Django-Channel')