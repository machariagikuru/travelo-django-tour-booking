from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'email', 'phone', 'travelers', 'in_date', 'out_date', 'created_at')
    list_filter = ('in_date', 'out_date', 'destination')
    search_fields = ('name', 'email', 'phone', 'destination__destination_name')
    ordering = ('-created_at',)

    fieldsets = (
        ("Booking Details", {
            'fields': ('destination', 'name', 'email', 'phone', 'travelers', 'notes')
        }),
        ("Trip Schedule", {
            'fields': ('in_date', 'out_date')
        }),
        ("System Info", {
            'fields': ('created_at',),
        }),
    )
    readonly_fields = ('created_at',)
    
    
admin.site.register(Booking,BookingAdmin)
