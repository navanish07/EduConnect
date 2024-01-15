from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Room, Topic    # Import Room model from models.py
from .forms import RoomForm # Import RoomForm from forms.py
from django.contrib.auth import authenticate, login, logout


# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Room 11'},
#     {'id': 2, 'name': 'Room 22'},
#     {'id': 3, 'name': 'Room 33'},
# ]

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: 
            messages.error(request, 'Username OR password is incorrect')


    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''    # Get query from url if it exists, else set q to empty string

    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
        )  # Get all rooms from database
    topics = Topic.objects.all() # Get all topics from database

    context = {
        'rooms': rooms,
        'topics': topics,
        'room_count': rooms.count(),
    }
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)  # Get room from database with id=pk (primary key)
    
    context = { 'room': room }
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()   # Create RoomForm object with no data which will be passed to template
    if request.method == 'POST':    # If request method is POST (form submitted)
        form = RoomForm(request.POST)   # Create RoomForm object with POST data
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}   # Create empty context dictionary
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)  # Get room from database with id=pk (primary key)
    form = RoomForm(instance=room)  # Create RoomForm object with room data which will be passed to template
    if request.method == 'POST':    # If request method is POST (form submitted)
        form = RoomForm(request.POST, instance=room)   # Create RoomForm object with POST data and room data (instance) 
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk) 
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room.name})    
    