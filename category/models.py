from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name       = models.CharField(max_length=50, unique=True)
    slug                = models.SlugField(max_length=150, unique=True)
    description         = models.TextField(max_length=250, blank=True)
    is_available        = models.IntegerField(blank=True, null=True)
    category_img        = models.ImageField(upload_to='photos/categories', blank=True)
    
    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
    
    def __str__(self):
        return self.category_name
