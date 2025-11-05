from django.db import models

class Hotel(models.Model):
    hotel_name          = models.CharField(max_length=100, unique=True)
    slug                = models.SlugField(max_length=155, unique=True)
    location            = models.TextField(max_length=255, blank=True)
    rent                = models.IntegerField()
    images              = models.ImageField(upload_to='photos/hotels')
    is_available        = models.BooleanField(default=True)
    rent_for            = models.CharField(max_length=100, blank=True, null=True)
    near_by             = models.CharField(max_length=100, blank=True, null=True)
    days                = models.IntegerField(blank=True, null=True)

    
    def __str__(self):
        return self.hotel_name
