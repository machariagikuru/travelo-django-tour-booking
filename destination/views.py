from django.shortcuts import get_object_or_404, render
from category.models import Category
from herosection.models import HeroSection
from .models import Destination
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def destination (request):
    destinations = Destination.objects.all()
    categories = Category.objects.filter(is_available = True)
    hero = HeroSection.objects.first()
    
    
    paginator = Paginator(destinations, 4)
    page = request.GET.get('page')
    paged_destination = paginator.get_page(page)
    destinations_count = destinations.count()
    
    context = {
        'destination': destinations,
        'category': categories,
        'destinations_count' : destinations_count,
        'paged_destination' : paged_destination,
        'hero':hero
    }
    return render(request, 'destination.html', context)



def destination_detail(request, slug):
    # Fetch the destination by slug
    dest = get_object_or_404(Destination, slug=slug)
    context = {
        'destination': dest,
    }
    return render(request, 'destination_detail.html', context)
