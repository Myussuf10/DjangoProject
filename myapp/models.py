import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class PostMessage(models.Model):
	choice = (('Politics', 'Politics'), ('Health', 'Health'),('Sport', 'Sport'),
	('Tech', 'Tech'))
	like = (('Liked','Liked'),('Disliked','Disliked'))
	user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
	title= models.CharField(max_length=100, blank=True)
	message = models.TextField(blank = True)
	expiry = models.DurationField(null=True)
	topic= models.CharField(default='Tech', choices=choice, max_length=50)
	created = models.DateTimeField(auto_now_add=True, null=True )
	status= models.BooleanField(default=True)
	def __str__(self):
		return self.title

class Interaction(models.Model):
	choice = (('Like','Like'),('Disliked','Disliked'))
	comment= models.TextField(blank = True)
	user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
	liked= models.CharField(blank = True,max_length=10, choices=choice)
	post = models.ForeignKey(PostMessage, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add = True, blank=True)
	def __str__(self):
		return self.comment
