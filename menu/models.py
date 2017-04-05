from __future__ import unicode_literals

from django.db import models

class Order(models Model):
	user_id = models.IntegerField()
	item_name = models.CharField(max_length=128)
	restaurant_name = models.CharField(max_length=128)

	def __str__(self):
		return self.user_id + ' ' + self.item_name + ' '+  self.restaurant_name

	def __unicode__(self):
		return self.user_id + ' ' + self.item_name + ' '+  self.restaurant_name
