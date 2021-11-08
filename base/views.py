from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# views

# rooms = [
#     {'id': 1, 'name': "Let's learn Python"},
#     {'id': 2, 'name': "Devs"},
#     {'id': 3, 'name': 'Lets learn JS'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    template_name = 'base/home.html'
    return render(request, template_name, context)


def room(request, pk):
    room = Room.objects.get(pk=pk)
    context = {'room': room}
    template_name = 'base/room.html'
    return render(request, template_name, context)
