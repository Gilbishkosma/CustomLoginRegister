from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('list/',views.UserListView.as_view(),name='userlist'),
    path('update/<int:pk>',views.UserUpdateView.as_view(),name='userupdate')
]