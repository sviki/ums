from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .serializers import LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from airbnb.serializers import ContentSerializer
from airbnb.models import *

def index(request):
    return HttpResponseRedirect(reverse('airbnb_list'))

class ContentViewSet(viewsets.ModelViewSet):
    queryset = PageContent.objects.all()
    serializer_class = ContentSerializer

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('airbnb_list'))
        else:
            context["error"] = "Provide valid credentials"
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)

@login_required(login_url='/login/')
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "auth/success.html", context)

def user_logout(request):
    context = {}
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))
    else:
        return render(request, "auth/login.html", context)

@login_required(login_url='/login/')
def airbnb_list(request):
    context = {}
    context['pagecontents'] = PageContent.objects.all()
    context['title'] = 'Airbnb'
    return render(request, 'airbnb/index.html', context)


class AirbnbView(APIView):
    def get(self, request):
        pagecontents = PageContent.objects.all()
        serializer = ContentSerializer(pagecontents, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = ContentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)
