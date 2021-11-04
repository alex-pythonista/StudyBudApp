from django.shortcuts import render
from django.http import HttpResponse


# views

rooms = [
    {'id': 1, 'name': "Let's learn Python"},
    {'id': 2, 'name': "Devs"},
    {'id': 3, 'name': 'Lets learn JS'},
]

def home(request):

    context = {}
    template_name = 'base/home.html'
    return render(request, template_name, context)


def room(request):
    
    context = {'rooms': rooms}
    template_name = 'base/room.html'
    return render(request, template_name, context)
