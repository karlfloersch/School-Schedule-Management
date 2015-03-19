from django.db import models

# Create your models here.
class Student(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	# Schedule

class Administrator(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	# pending_requests

