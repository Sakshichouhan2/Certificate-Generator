from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student_Details(models.Model):
	#loginid = models.CharField(max_length=50, unique=True)
	#password = models.CharField(max_length=50)
	fullname = models.CharField(max_length=100)
	contact_no = models.CharField(max_length=15)
	alternate_contact_no = models.CharField(max_length=15,null=True)
	course = models.CharField(max_length=150)
	address = models.TextField()

	def __str__(self):
		return self.fullname
