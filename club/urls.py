from django.contrib import admin
from django.urls import path
from .views import home_page, skate, club_member, show_news, show_detail

urlpatterns = [
    path('', home_page, name='home'),
    path('kind_of_sk/', skate, name='skate'),
    path('club_members/', club_member, name='members'),
    path('news/', show_news, name='news'),
    path('news/detail/<pk>/', show_detail, name='show_detail')
]