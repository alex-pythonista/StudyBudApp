from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

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


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')

    context = {'form': form}
    template_name = 'base/room_form.html'
    return render(request, template_name, context)


def updateRoom(request, pk):
    room = Room.objects.get(pk=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('base:home')

    context = {'form': form}
    template_name = 'base/room_form.html'
    return render(request, template_name, context)


def deleteRoom(request, pk):
    room = Room.objects.get(pk=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('base:home')

    context = {'obj': room}
    template_name = 'base/delete.html'
    return render(request, template_name, context)