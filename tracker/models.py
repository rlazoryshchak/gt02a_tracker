from __future__ import unicode_literals

from django.db import models

class Point(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    created_at = models.DateTimeField()

    @staticmethod
    def by_day(day):
        from_time = day + ' 00:00'
        to_time = day + ' 23:59'
        return Point.objects.filter(created_at__range=[from_time, to_time])