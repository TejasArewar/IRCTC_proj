from django.shortcuts import render, redirect
from App.models import Trains, Booking
from Accounts.models import Passenger_register
import random
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,"index.html")


def trains(request):
    train = Trains.objects.all()
    return render(request,"trains.html", {'train':train})


def available_train(request):
    if request.method == 'POST':
        from_station = request.POST.get('from')
        to_station = request.POST.get('to')
        date = request.POST.get('date')
        avl_trains = Trains.objects.filter(
            Q(from_station__icontains=from_station) & 
            Q(to_station__icontains=to_station)
        )

        return render(request, 'available_train.html', {'avl_trains': avl_trains, 'date': date})
    return render(request, 'index.html')


def book(request,id) :
    book_ticket = Trains.objects.get(id = id)
    return render(request, 'booking.html', {'book_ticket' : book_ticket})



def booking(request,id, from_station, to_station) :
    passenger_id = request.session.get('id')
    passenger = Passenger_register.objects.get(id=passenger_id)
    train_name = Trains.objects.get(id=id)
    seats = train_name.seats
    try:
        booking_count = Booking.objects.all().count()
        if booking_count < seats:
            seat_no = 'S'+booking_count//72+''+booking_count%72
            waiting_no = 0
            status = 'reserved'
            pnr = random.randint(999999999,10000000000)
            booking = Booking.objects.create(passenger=passenger,train_name=train_name,pnr=pnr,seat_no=seat_no,status=status,waiting_no=waiting_no,from_station=from_station,to_station=to_station)
            booking.save()

        else:
            seat_no = 0
            waiting_no = booking_count-seats+1
            status = 'waiting'
            pnr = random.randint(999999999,10000000000)
            booking = Booking.objects.create(passenger=passenger,train_name=train_name,pnr=pnr,seat_no=seat_no,status=status,waiting_no=waiting_no,from_station=from_station,to_station=to_station)
            booking.save()

    except ObjectDoesNotExist:
        seat_no = 1
        waiting_no = 0
        status = 'reserved'
        pnr = random.randint(999999999,10000000000)
        booking = Booking.objects.create(passenger=passenger,train_name=train_name,pnr=pnr,seat_no=seat_no,status=status,waiting_no=waiting_no,from_station=from_station,to_station=to_station)
        booking.save()

        
    return render(request, 'booking.html', {'booking':booking})