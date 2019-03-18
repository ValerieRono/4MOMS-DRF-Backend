from django.shortcuts import render
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from babies.models import Babies
from babies.serializers import BabiesSerializer
from babies.permissions import IsParent


# Create your views here.
class BabiesList(ListCreateAPIView):
    """
    List all babies, or create a new baby.
    """
    permission_classes = (IsAuthenticated, IsParent)
    serializer_class = BabiesSerializer

    def perform_create(self, serializer):
        serializer.save(parent=self.request.user)

    def get_queryset(self):
        """
        This view should return a list of all the babies
        for the currently authenticated user.
        """
        user = self.request.user
        return Babies.objects.filter(parent=user)
            

class BabiesDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrive, update or delete a baby instance
    """
    permission_classes = (IsAuthenticated, IsParent)
    queryset = Babies.objects.all()
    serializer_class = BabiesSerializer
