from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]