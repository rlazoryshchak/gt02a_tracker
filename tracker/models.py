from __future__ import unicode_literals

from django.db import models

class Point(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)