from django.urls import path

from measurement.views import SensorListCreateView, MeasurementCreateView, SensorUpdateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
]
