from django.shortcuts import render
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import CustomUser
# Create your views here.

class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

class UserListView(ListView):
	model = CustomUser
	template_name = "user_list.html"

# class UserUpdateView(UpdateView):
# 	model = CustomUser
# 	fields = ["username",""]
# 	template_name = "user_update.html"