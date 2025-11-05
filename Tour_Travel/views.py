from aboutussection.models import AboutSection
from herosection.models import HeroSection
from packages.models import Packages
from gallery.models import Gallery
from django.shortcuts import render
from category.models import Category
from destination.models import Destination
from reviews.models import Review
from servicesection.models import Service,ServicesHeader

def home(request):
    category = Category.objects.all()
    destination = Destination.objects.all()
    packages = Packages.objects.all().order_by('-created_at')[:3]
    gallery = Gallery.objects.all()
    reviews = Review.objects.select_related("destination").order_by("-created_at")[:5]
    hero = HeroSection.objects.first()
    services_header = ServicesHeader.objects.first()
    services = Service.objects.all()[:4]
    
    context = {
        "category": category,
        "destination": destination,
        "reviews": reviews,
        'packages': packages,
        'gallery':gallery,
        'hero':hero,
        'services_header':services_header,
        'services':services,
    }
    
    return render(request, "home.html",context)

def about(request):
    reviews = Review.objects.select_related("destination").order_by("-created_at")[:5]
    hero = HeroSection.objects.first()
    services_header = ServicesHeader.objects.first()
    services = Service.objects.all()[:4]
    about = AboutSection.objects.first()
    
    context = {
        "reviews": reviews,
        'hero':hero,
        'services_header':services_header,
        'services':services,
        'about':about,
    }
    return render(request,'about.html',context)