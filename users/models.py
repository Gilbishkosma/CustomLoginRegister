from django.db import models
from django.contrib.auth.models import AbstractUser
from app.models import State,Education,Interest

# Create your models here.

Gender_choices = [('Male','Male'),('Female','Female')]

class CustomUser(AbstractUser):
	sex = models.CharField(max_length=100,choices=Gender_choices,null=True,blank=False,default='Male')
	state = models.ForeignKey(State,on_delete=models.DO_NOTHING,related_name='userstate',null=True,blank=False)
	education = models.ManyToManyField(Education,verbose_name="education select",blank=True)
	interest = models.ForeignKey(Interest,on_delete=models.DO_NOTHING,related_name="userinterest",null=True,blank=False)