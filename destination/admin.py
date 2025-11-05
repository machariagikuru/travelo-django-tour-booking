from django.contrib import admin
from .models import Destination

class destinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('destination_name',)}
    list_display = ('destination_name', 'days', 'price', 'hotel', 'near_by','is_available')

admin.site.register(Destination,destinationAdmin)
