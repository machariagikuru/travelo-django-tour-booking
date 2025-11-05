from django.contrib import admin
from .models import Gallery

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')
