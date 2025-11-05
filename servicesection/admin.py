from django.contrib import admin
from .models import ServicesHeader, Service

@admin.register(ServicesHeader)
class ServicesHeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class', 'color_class')
