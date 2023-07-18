from django.db import models

from apps.utils.generics.models import BaseModel


class Business(BaseModel):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
