from django.contrib import admin
from .models import Packages, BookingPackage, Itinerary

@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'price', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'destination')

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('package', 'day', 'title')
    list_filter = ('package',)
    ordering = ('package', 'day')

@admin.register(BookingPackage)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'package', 'first_name', 'email', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
