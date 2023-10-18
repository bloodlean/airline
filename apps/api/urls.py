from django.urls import path, include
from .views import *

urlpatterns = [
    path('plane/', PlaneAPIView.as_view()),
    path('plane/<int:pk>/', PlaneDetailAPIView.as_view()),
    path('airline/', AirlineAPIView.as_view()),
    path('airline/<int:pk>/', AirlineDetailAPIView.as_view()),
    path('flight/', FlightAPIView.as_view()),
    path('flight/<int:pk>/', FlightDetailAPIView.as_view()),

    path('auth/', include('dj_rest_auth.urls'))
]