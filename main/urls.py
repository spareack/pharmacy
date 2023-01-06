from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_medicines', views.get_medicines, name='get_medicines'),
]
