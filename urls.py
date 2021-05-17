from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vnos', views.vnos, name='vnos'),

]