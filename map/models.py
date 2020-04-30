from django.contrib.gis.db import models


class Point(models.Model):
    pointer = models.PointField()

    class Meta:
        verbose_name = 'Point'
        verbose_name_plural = 'Points'
