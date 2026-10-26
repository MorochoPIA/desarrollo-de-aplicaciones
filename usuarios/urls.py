from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.inicio_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('panel/', views.panel, name='panel'),
]