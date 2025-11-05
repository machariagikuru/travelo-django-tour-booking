from django.contrib import admin
from .models import AboutSection

class aboutSection(admin.ModelAdmin):
    list_display = ('title','subtitle',)

admin.site.register(AboutSection,aboutSection)
