from django.urls import path
from . import views

urlpatterns = [
    path('', views.empleado, name="empleado"),
    path('tickets_emitidos/', views.tickets_emitidos, name="tickets_emitidos"),
    #path('lista_productos/', views.lista_productos, name="lista_productos"),
]