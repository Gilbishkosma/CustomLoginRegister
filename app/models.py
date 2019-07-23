from django.db import models

# Create your models here.



class State(models.Model):
	statename = models.CharField(max_length=100)

	def __str__(self):
		return self.statename


class Education(models.Model):
	education = models.CharField(max_length=100)

	def __str__(self):
	    return self.education

class Interest(models.Model):
	interest = models.CharField(max_length=100)

	def __str__(self):
		return self.interest