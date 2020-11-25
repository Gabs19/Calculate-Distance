from django.urls import path
from .views import calculte_distance_view

app_name = 'measurements'

urlpatterns = [
    path('',calculte_distance_view, name = 'calculate-view'),
]