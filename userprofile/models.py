from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance. 
	user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    location = models.CharField(max_length = 128)
    phone_number = models.IntegerField()
    picture = models.ImageField(upload_to='profile_images', blank=True)

	# Override the __unicode__() method to return out something meaningful! 
	# Remember if you use Python 2.7.x, define __unicode__ too!
	def __str__(self):
		return self.user.username

	def __unicode__(self):
		return self.user.username