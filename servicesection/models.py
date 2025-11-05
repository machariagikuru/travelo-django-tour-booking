from django.db import models

# For the right-side text block
class ServicesHeader(models.Model):
    subtitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    paragraph_1 = models.TextField(blank=True, null=True)
    paragraph_2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


# For each individual service card
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(
        max_length=100,
        help_text="e.g. 'flaticon-paragliding' or 'flaticon-map'"
    )
    background_image = models.ImageField(upload_to='services/')
    color_class = models.CharField(
        max_length=20,
        default='color-1',
        help_text="e.g. color-1, color-2, color-3..."
    )

    def __str__(self):
        return self.title
