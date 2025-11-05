from django.db import models
from category.models import Category
from hotel.models import Hotel

class Destination(models.Model):
    destination_name    = models.CharField(max_length=100, unique=True)
    slug                = models.SlugField(max_length=155, unique=True)
    description         = models.TextField(max_length=255, blank=True)
    price               = models.IntegerField()
    days                = models.IntegerField()
    images              = models.ImageField(upload_to='photos/destination')
    is_available        = models.BooleanField(default=True)
    hotel               = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    category            = models.ForeignKey(Category, on_delete=models.CASCADE)
    in_date             = models.DateField()
    out_date            = models.DateField()
    near_by             = models.CharField(max_length=100, blank=True)
    
    
    def __str__(self):
        return self.destination_name
