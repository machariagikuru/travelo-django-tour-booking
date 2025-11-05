from django.db import models
from destination.models import Destination

class Booking(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    travelers = models.PositiveIntegerField()
    in_date = models.DateField()
    out_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.name} for {self.destination.destination_name}"
