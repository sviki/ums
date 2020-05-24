"""ums URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from airbnb.views import user_login, user_logout, success, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', include('airbnb.urls')),
    path('airbnb/', include('airbnb.urls')),
    path('api/v1/', include('airbnb.api_urls')),
    path('api/v1/auth/login/', LoginView.as_view()),
    path('api/v1/auth/logout/', LogoutView.as_view()),

    path('login/', user_login, name="user_login"),
    path('success/', success, name="user_success"),
    path('logout/', user_logout, name="user_logout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
