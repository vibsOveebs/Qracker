from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    FOOD_OR_DRINK_CHOICES = (
        ('Food', 'Food'),
        ('Drink', 'Drink')
    )
    name = models.CharField(max_length=100)
    #food_or_drink = models.CharField(max_length=5, choices=FOOD_OR_DRINK_CHOICES)
    is_breakfast = models.BooleanField(default=False)
    is_lunch = models.BooleanField(default=False)
    promo_flag = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    supplier = models.ForeignKey(User)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Order(models.Model):
    user_name = models.CharField(max_length=128)
    item_name = models.CharField(max_length=128)
    restaurant_name = models.CharField(max_length=128)
    creation_time = models.DateTimeField()

    def __str__(self):
        return self.user_name + ' ' + self.item_name + ' ' + self.restaurant_name

    def __unicode__(self):
        return self.user_name + ' ' + self.item_name + ' ' + self.restaurant_name
