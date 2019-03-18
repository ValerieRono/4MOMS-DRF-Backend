from django.shortcuts import render 
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from babies.models import Babies
from tracker.models import Tracker
from tracker.serializers import TrackerSerializer


# Create your views here.
class TrackerList(ListCreateAPIView):
    """
    List all records, or create a new record.
    """
    serializer_class = TrackerSerializer

    def perform_create(self, serializer):
        name = self.kwargs['name']
        baby = Babies.objects.get(name=name)
        serializer.save(baby=baby)

    def get_queryset(self):
        """
        restrics returned records to a given baby
        by filtering against a 'name' query parameter in the URL.
        """
        queryset = Tracker.objects.all()
        name = self.kwargs['name']
        queryset = queryset.filter(baby__name=name)
        return queryset
     
class TrackerDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrive, update or delete a record instance
    """
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer

