from django.db import models
from attractions_info.models import AttractionsInfo
from reviews.models import Review
from address.models import Address

# Create your models here.


class Attraction(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions_info = models.ManyToManyField(AttractionsInfo)
    reviews = models.ManyToManyField(Review)
    image = models.ImageField(upload_to="attractions", null=True, blank=True)
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name
