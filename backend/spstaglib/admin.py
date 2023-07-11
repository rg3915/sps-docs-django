from django.contrib import admin

from .models import SPSElement


@admin.register(SPSElement)
class SPSElementAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'description')
    search_fields = ('name', 'title', 'description')
