from django.contrib import admin
from .models import HeroSection

class heroSection(admin.ModelAdmin):
    list_display = ('title','subtitle',)

admin.site.register(HeroSection,heroSection)
