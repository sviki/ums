from django.urls import path, include
from rest_framework import routers

from airbnb.views import *

router = routers.DefaultRouter()
router.register('', ContentViewSet)

urlpatterns = [
    path('airbnb/', include(router.urls)),    
]

