from django.db import models

class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('destination', 'Destination'),
        ('hotel', 'Hotel'),
        ('traveler', 'Traveler Moments'),
        ('drone', 'Drone Shots'),
    ]

    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
