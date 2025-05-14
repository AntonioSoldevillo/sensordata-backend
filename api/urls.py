from django.urls import path
from .views import SensorDataListCreateView

urlpatterns = [
    path('sensor-data/', SensorDataListCreateView.as_view(), name='sensor-data'),
]
