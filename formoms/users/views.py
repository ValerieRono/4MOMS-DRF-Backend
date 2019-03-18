from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsAdminUser, IsOwnerOrIsAdmin


# Create your views here.
class UsersList(ListCreateAPIView):
    """
    List all users, or create a new User.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        self.permission_classes = []
        if self.request.method == 'GET':
            self.permission_classes = [IsAdminUser,]
        else:
            self.permission_classes = []

        return super(UsersList, self).get_permissions()

class UserDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrive, update or delete a user instance
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        self.permission_classes = []
        if self.request.method == 'DELETE':
            self.permission_classes = [IsAdminUser,]
        else:
            self.permission_classes = [IsAuthenticated, IsOwnerOrIsAdmin]

        return super(UserDetail, self).get_permissions()
