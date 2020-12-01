from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<nombre_ciudad>/', views.eliminar_ciudad, name='eliminar_ciudad'),
    path('dias/<str:nombre>/', views.pronostico, name='dias'),
]
