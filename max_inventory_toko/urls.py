from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='max_inventory_toko.index'),
]