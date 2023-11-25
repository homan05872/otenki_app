from django.urls import path 
from . import views


urlpatterns = [
    path('top/', views.TopView.as_view()),
    path('api/<int:pk>', views.WeatherAPIView.as_view()),
]
