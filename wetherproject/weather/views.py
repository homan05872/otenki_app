from django.shortcuts import render
from django.views.generic import ListView
from . models import Weather

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import WeatherSerializer

class TopView(ListView):
    template_name = 'top.html'
    model = Weather


class WeatherAPIView(RetrieveAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [IsAuthenticated]