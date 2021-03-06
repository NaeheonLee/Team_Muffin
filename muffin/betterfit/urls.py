from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generic', views.generic, name='generic'),
    path('elements', views.elements, name='elements'),
    path('mannequin', views.mannequin, name='mannequin'),
    path('women', views.women, name='women'),
]