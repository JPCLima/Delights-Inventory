from django.db import models


class Ingredient(models.Model):
    """Represents a single Ingredient"""
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=100)
    price_unit = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/ingredients"
