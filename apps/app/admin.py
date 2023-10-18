from django.contrib import admin
from .models import *

@admin.register(Plane)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'From')
    list_display_links = ('id', 'From')