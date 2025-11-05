from django.db import models
from django.utils import timezone


# 🌍 PACKAGES MODEL
class Packages(models.Model):
    CATEGORY_CHOICES = [
        ('honeymoon', 'Honeymoon'),
        ('family', 'Family'),
        ('adventure', 'Adventure'),
        ('weekend', 'Weekend Getaway'),
        ('luxury', 'Luxury'),
        ('budget', 'Budget'),
    ]

    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    days = models.IntegerField()
    nights = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='packages/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.destination}"


# 🗓️ ITINERARY MODEL
class Itinerary(models.Model):
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name='itineraries')
    day = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"Day {self.day} - {self.title} ({self.package.title})"


# 🧳 BOOKING MODEL
class BookingPackage(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    package = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name='bookings')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    number_of_travelers = models.PositiveIntegerField(default=1)
    start_date = models.DateField()
    room_type = models.CharField(max_length=50, blank=True, null=True)
    special_requests = models.TextField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Booking #{self.id} - {self.first_name} {self.last_name} ({self.package.title})"
