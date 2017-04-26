from __future__ import unicode_literals
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db import models
from menu.models import Item
from random import randint


# random code generator
def generate_code():
    return randint(0,9999)


# Transaction Model
class Transaction(models.Model):

    # Transactions entity
    creation_time = models.DateTimeField()
    delivery_time = models.DateTimeField(blank=True, null=True)
    pickup_loc = models.CharField(max_length=64)

    # item in transaction fields
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()

    code = models.IntegerField(default=generate_code)

    # Initiates and Delivers relationships
    initiates = models.ForeignKey(User, related_name='initiates')
    delivers = models.ForeignKey(User, related_name='delivers', blank=True, null=True)

    # Feedback entity
    timeliness = models.IntegerField(blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    friendliness = models.IntegerField(blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    responsetime = models.IntegerField(blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    text_feedback = models.CharField(blank=True, null=True, max_length=140)

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)
