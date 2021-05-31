from django.db import models

class Meter(models.Model):
    iter = models.IntegerField()
    value = models.FloatField()
