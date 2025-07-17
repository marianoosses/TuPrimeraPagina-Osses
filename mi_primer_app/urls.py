from django.urls import path

from .views import saludo, saludo_con_template, crear_familiar, inicio
                    

urlpatterns = [
    path('',inicio, name='inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/<str:nombre>/', crear_familiar),
]
