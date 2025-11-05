from django.db import models
from destination.models import Destination

class Review(models.Model):
    destination         = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='reviews')
    name                = models.CharField(max_length=100)
    rating              = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review              = models.TextField()
    created_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating}/5) - {self.destination.destination_name}"