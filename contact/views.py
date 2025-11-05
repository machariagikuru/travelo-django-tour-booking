from django.shortcuts import render, redirect
from herosection.models import HeroSection
from .forms import ContactForm

def contact(request):
    hero = HeroSection.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data into the database
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'hero':hero})

def contact_success(request):
    return render(request, 'success.html')
