from django.shortcuts import render
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm,CustomUserUpdateForm
from .models import CustomUser
# Create your views here.

class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'


class UserListView(LoginRequiredMixin,ListView):
	model = CustomUser
	template_name = "user_list.html"

class UserUpdateView(LoginRequiredMixin,UpdateView):
	model = CustomUser
	form_class = CustomUserUpdateForm
	template_name = "user_update.html"
	success_url = reverse_lazy("userlist")