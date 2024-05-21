from django.db import models
from authentication.models import User

class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=100, decimal_places=2)
    location = models.CharField(max_length=100)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    hospitals_nearby = models.BooleanField(default=False)
    colleges_nearby = models.BooleanField(default=False)

    def __str__(self):
        return self.place
