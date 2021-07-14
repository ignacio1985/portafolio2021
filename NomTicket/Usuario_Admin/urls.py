"""NomTicket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    #path('', views.inicio,name="inicio"),
    path('registrar/', views.registrar_empleado, name="registrar_empleado"),
    #path('<int:id>/', views.registrar_empleado, name="modificar_empleado"),
    path('eliminar_empleado/<id>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('lista/', views.lista_empleado, name="lista_empleado"),
    path('home_admin/', views.home_admin, name="home_admin"),
    path('login_admin/',LoginView.as_view(template_name='login_admin.html'), name="login_admin"),
    path('modificar_empleado/<id>',views.modificar_empleado, name='modificar_empleado'),
    path('contacto/', views.enviarcorreo, name='contacto'),
    path('tickets_empleados/',views.tickets_empleados,name='tickets_empleados'),
    path('tickets_visitantes/',views.tickets_visitantes,name='tickets_visitantes'),
]
