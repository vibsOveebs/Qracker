from __future__ import unicode_literals

from django.db import models

from datetime import datetime

class Order(models.Model):
	user_name = models.CharField(max_length=128)
	item_name = models.CharField(max_length=128)
	restaurant_name = models.CharField(max_length=128)
	creation_time = models.DateTimeField()

	def __str__(self):
		return self.user_name + ' ' + self.item_name + ' '+  self.restaurant_name

	def __unicode__(self):
		return self.user_name + ' ' + self.item_name + ' '+  self.restaurant_name
