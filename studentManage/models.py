from django.db import models
from django.contrib.auth.models import User,UserManager

# Create your models here.
class Adminer(models.Model):
	username=models.EmailField(max_length=30, default="", unique=True)
	password=models.CharField(max_length=30)

	def __unicode__(self):
        		return self.username