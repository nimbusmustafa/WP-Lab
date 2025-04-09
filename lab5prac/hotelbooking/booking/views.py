from django.shortcuts import render, redirect
from .models import Room, Customer
from .forms import BookingForm

def home(request):
    return render(request, 'home.html')

def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            customer = form.save()
            room = customer.room
            room.status = 'Allotted'
            room.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'book_room.html', {'form': form})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})
