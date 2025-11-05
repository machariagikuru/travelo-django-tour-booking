from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from herosection.models import HeroSection
from .models import Review
from destination.models import Destination

def write_review(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    hero = HeroSection.objects.first()

    if request.method == "POST":
        name = request.POST['name']
        rating = request.POST['rating']
        review = request.POST['review']

        Review.objects.create(
            destination=destination,
            name=name,
            rating=rating,
            review=review
        )

        messages.success(request, "Thank you for your review!")
        return redirect('destination_detail', slug=destination.slug)


    return render(request, 'review.html', {'destination': destination, 'hero':hero})
