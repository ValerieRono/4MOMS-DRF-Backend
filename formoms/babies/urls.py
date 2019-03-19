from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from babies import views

urlpatterns = [
    path('babies/', views.BabiesList.as_view(), name='baby-list'),
    path('babies/<int:pk>/', views.BabiesDetail.as_view(), name='baby-detail')
]