from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'rating', 'created_at')
    list_filter = ('rating', 'destination')
    search_fields = ('name', 'review', 'destination__destination_name')
    ordering = ('-created_at',)

    fieldsets = (
        ("Reviewer Info", {
            'fields': ('name', 'destination')
        }),
        ("Review Details", {
            'fields': ('rating', 'review')
        }),
        ("System Info", {
            'fields': ('created_at',),
        }),
    )
    readonly_fields = ('created_at',)
    
    
admin.site.register(Review,ReviewAdmin)
