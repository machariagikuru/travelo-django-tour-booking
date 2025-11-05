from django.shortcuts import render

from herosection.models import HeroSection
from .models import Gallery

def gallery_view(request):
    category = request.GET.get('category')
    hero = HeroSection.objects.first()
    if category:
        images = Gallery.objects.filter(category=category)
    else:
        images = Gallery.objects.all()

    context = {
        'images': images,
        'categories': Gallery.CATEGORY_CHOICES,
        'hero':hero
    }
    return render(request, 'gallery.html', context)
