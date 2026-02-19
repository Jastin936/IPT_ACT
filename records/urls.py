from django.urls import path
from . import views  # This imports your views.py file

urlpatterns = [
    path('add/', views.add_record, name='add_record'),
    path('show/', views.show_records, name='show_records'),
]