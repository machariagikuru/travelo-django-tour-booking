from django.shortcuts import render

from herosection.models import HeroSection
from .models import Hotel

def hotel (request):
    hotels = Hotel.objects.filter(is_available=True)
    hero = HeroSection.objects.first()
    
    context = {
        'hotels' : hotels,
        'hero':hero,
    }
    return render(request,'hotel.html',context)