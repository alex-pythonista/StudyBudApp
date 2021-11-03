from django.shortcuts import render
from django.http import HttpResponse


# views

def home(request):
    return HttpResponse('Home page')


def room(request):
    return HttpResponse('Rooms!!')
