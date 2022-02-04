from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('<int:pk>/delete/', views.car_delete, name='car_delete'),
    path('add/', views.car_add, name='car_add'),
]