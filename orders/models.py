from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from menu.models import Item

from django.core.validators import MaxValueValidator, MinValueValidator

from random import randint


def generate_code():
    return randint(0,9999)

class Transaction(models.Model):
    # Transactions entity
    creation_time = models.DateTimeField()
    delivery_time = models.DateTimeField(blank=True, null=True)
    pickup_loc = models.CharField(max_length=64)

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
        return id

    def __unicode__(self):
        return id
