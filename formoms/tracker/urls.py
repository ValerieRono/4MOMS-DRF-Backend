from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tracker import views

urlpatterns = [
    path('babies/<slug:name>', views.TrackerList.as_view(), name='tracker-list'),
    path('babies/<slug:name>/<int:pk>', views.TrackerDetail.as_view(), name='tracker-detail')
]