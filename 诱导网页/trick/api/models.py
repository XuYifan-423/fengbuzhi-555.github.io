from django.db import models

# Create your models here.
class Visits(models.Model):
    times = models.IntegerField(default=0)

class Clicks(models.Model):
    times = models.IntegerField(default=0)

