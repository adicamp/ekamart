from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='master_user.index'),
]