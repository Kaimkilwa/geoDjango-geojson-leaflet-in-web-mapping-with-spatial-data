
from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from djgeojson.fields import PointField



class ChurchDetails(models.Model):
    name = models.CharField(max_length=100)
    geom = models.PointField(srid= 4128)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    # objects = models.GeoManager()
    picture = models.ImageField(  upload_to='images',null= True, blank=True)

    @property
    def PopupContent(self):
        return '<img src="{}" /><p><{}</p>'.format(
            self.picture.url,
            self.name)

    @property
    def lat_lon(self):
        return list(getattr(
            self.geom,
            'coords', [])[::-1])

