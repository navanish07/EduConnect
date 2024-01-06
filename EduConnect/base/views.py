from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id': 1, 'name': 'Room 11'},
    {'id': 2, 'name': 'Room 22'},
    {'id': 3, 'name': 'Room 33'},
]


def home(request):
    context = {
        'rooms': rooms
    }
    return render(request, 'base/home.html', context)

def room(request, pk):
    return render(request, 'base/room.html')