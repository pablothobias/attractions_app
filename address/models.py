from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode =  models.CharField(max_length=7)
    complement = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.street} - {self.city} - {self.state}"

