from django.urls import path
from airbnb.views import *

urlpatterns = [
    path('', airbnb_list, name='airbnb_list'),
]