from django.contrib import admin
from hotel.models import Hotel

class hotelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('hotel_name',)}
    list_display = ('hotel_name', 'rent', 'rent_for', 'near_by','location', 'is_available',)

admin.site.register(Hotel,hotelAdmin)
