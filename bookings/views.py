from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from herosection.models import HeroSection
from .models import Booking
from destination.models import Destination

def book_trip(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    hero = HeroSection.objects.first()

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        travelers = request.POST['travelers']
        in_date = request.POST['in_date']
        out_date = request.POST['out_date']
        notes = request.POST.get('notes', '')

        Booking.objects.create(
            destination=destination,
            name=name,
            email=email,
            phone=phone,
            travelers=travelers,
            in_date=in_date,
            out_date=out_date,
            notes=notes
        )

        messages.success(request, "Your booking has been confirmed!")
        return redirect('destination_detail', slug=destination.slug)


    return render(request, 'booking.html', {'destination': destination,'hero':hero})
