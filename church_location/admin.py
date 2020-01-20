from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import ChurchDetails
from  leaflet.admin import LeafletGeoAdmin

@admin.register(ChurchDetails,)
class ChurchAdmin(LeafletGeoAdmin):
    list_display = ('name', 'geom', 'picture')


