from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField()
    description = models.TextField()
    popular = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField()
    description = models.TextField()
    price = models.FloatField()
    price_currency = models.enums('$')
    discount_percentage = models.FloatField()
    discounted_price = models.FloatField()
    quantity = models.IntegerField()
    ratings = models.FloatField(
        validators=[
            MaxValueValidator(5.0),
            MinValueValidator(1.0)
        ]
    )
    popular = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
