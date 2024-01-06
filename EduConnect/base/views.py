from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Room    # Import Room model from models.py
from .forms import RoomForm # Import RoomForm from forms.py

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Room 11'},
#     {'id': 2, 'name': 'Room 22'},
#     {'id': 3, 'name': 'Room 33'},
# ]



def home(request):
    rooms = Room.objects.all()  # Get all rooms from database
    context = {
        'rooms': rooms
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
    