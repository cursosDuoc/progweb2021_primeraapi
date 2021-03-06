from django.shortcuts import render
from django.contrib.auth.models import User
from introapi.primeraapi.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.

class UserViewSet(viewsets.ModelViewSet) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]