from django.urls import path
from .views import *
urlpatterns = [
    path('', store, name='store'),
    path('<pk>/', store, name='store'),
    path('add/<product_id>/', add_to_cart, name='add'),
    path('add_quantity/<product_id>/',  add_quantity, name='add_quantity'),
    path('sub_quantity/<product_id>/',  sub_quantity, name='sub_quantity'),
    path('check_out/<cart_id>/', check_out, name='check_out')

]
