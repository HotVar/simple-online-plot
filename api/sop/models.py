from django.db import models

class Meter(models.Model):
    iter = models.IntegerField()
    train_val = models.FloatField()
    valid_val = models.FloatField()
