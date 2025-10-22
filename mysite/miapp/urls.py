from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('lista_calificaciones')), 
    path('calificaciones/', views.lista_calificaciones, name='lista_calificaciones'),
    path('calificaciones/crear/', views.crear_calificacion, name='crear_calificacion'),
    path('calificaciones/<int:id_calificacion>/editar/', views.actualizar_calificacion, name='actualizar_calificacion'),
    path('calificaciones/<int:id_calificacion>/eliminar/', views.eliminar_calificacion, name='eliminar_calificacion'),
    path('api/calificaciones/', views.api_calificaciones, name='api_calificaciones'),
]
