from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='jwk_toko.index'),
]