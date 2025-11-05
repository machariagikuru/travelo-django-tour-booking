from django.db import models

class AboutSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True, null=True)
    background_image = models.ImageField(upload_to='about/', blank=True, null=True)
    background_image2 = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.title
