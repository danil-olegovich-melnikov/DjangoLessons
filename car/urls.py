from django.urls import path
from . import views_car
from . import views_trip

app_name = 'car'

urlpatterns = [
    path('', views_car.car_list, name='car_list'),
    path('delete/<int:pk>', views_car.car_delete, name='car_delete'),
    path('add/', views_car.car_add, name='car_add'),
    path('put/', views_car.car_put, name='car_put'),
    path('<int:pk>/trips/add/', views_trip.trip_add, name='trip_add'),
    path('<int:pk>/trips/delete/<int:pk_trip>/', views_trip.trip_delete, name='trip_delete'),
    path('<int:pk>/trips/', views_trip.trip_list, name='trip_list'),
]