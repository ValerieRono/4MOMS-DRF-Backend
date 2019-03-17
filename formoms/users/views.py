from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.models import User
from users.serializers import UserSerializer

# Create your views here.
class UsersList(ListCreateAPIView):
    """
    List all users, or create a new User.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrive, update or delete a user instance
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
