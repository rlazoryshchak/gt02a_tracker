from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from mapbox import Directions
import os

class Point(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    created_at = models.DateTimeField()

    @staticmethod
    def by_day(day):
        day = day if day != '' else datetime.now().strftime('%Y-%m-%d')
        from_time = day + ' 00:00'
        to_time = day + ' 23:59'
        return Point.objects.filter(created_at__range=[from_time, to_time])

    @staticmethod
    def snap_to_road(received_point):
        service = Directions()
        coords = [received_point.lng, received_point.lat]
        origin = destination = {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [coords, coords]
            }    
        }
        response = service.directions([origin, destination], profile='mapbox.driving')
        try:
            coordinates = response.geojson()['features'][0]['geometry']['coordinates'][0]
        except IndexError:
            return received_point
        received_point.lat = coordinates[1]
        received_point.lng = coordinates[0]
        received_point.save()
        return received_point