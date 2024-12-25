from django.contrib import admin
from .models import Building

# Register your models here.
@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name','total_flats','location','occupancy','size')
    search_fields = ('name','location')
    list_filter = ('total_flats','occupancy','size')
    fields = ('name','total_flats','location','occupancy','size')
