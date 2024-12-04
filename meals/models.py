from django.db import models


class Meal(models.Model):
    meal_name = models.CharField(max_length=25)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=25)
    cuisine = models.CharField(max_length=20)
