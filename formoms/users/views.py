from django.shortcuts import render
from users.models import User
from users.serializers import UserSerializer
from rest_framework import generics

# Create your views here.
class UsersList(generics.ListCreateAPIView):
    """
    List all users, or create a new User.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrive, update or delete a user instance
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
