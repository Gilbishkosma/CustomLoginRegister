from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


Gender_choices = [('Male','Male'),('Female','Female')]

class CustomUserCreationForm(UserCreationForm):
	 class Meta(UserCreationForm.Meta):
	 	  model = CustomUser
	 	  fields = ('username','email','sex','state','education','interest')
	 	  widgets = {'sex':forms.RadioSelect(choices=Gender_choices)}



class CustomUserChangeForm(UserChangeForm):

	class Meta:
		 model = CustomUser
		 fields = ('username','email') #using default Meta fields


#UserCreationForm and UserChangeForm are the inbuilt classes of django default form
#We are just extending both
#UserCreationForm are used when we sign up
#UserchangeForm are used when we change something from admin site