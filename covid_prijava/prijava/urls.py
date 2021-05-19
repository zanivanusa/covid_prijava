from django.urls import path
from . import views


urlpatterns = [
    path('', views.prijava, name='prijava'),
    path('podatki/', views.prijava_podatki, name='podatki'),

]