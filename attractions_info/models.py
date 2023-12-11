from django.db import models

# Create your models here.

class AttractionsInfo(models.Model):
    name = models.CharField(max_length=40)
    descriptions = models.TextField()
    open_days = models.TextField()
    open_hour = models.TimeField()
    close_hour = models.TimeField()
    min_age_enter = models.IntegerField()


def __str__(self):
    return self.name
