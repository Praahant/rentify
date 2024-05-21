from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    # Add more URL patterns here
]