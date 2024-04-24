from django.urls import path, include
from . import views
from .views import *



urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('reportes/', views.reportes, name='reportes'),
    path('formulario/', views.formulario, name='formulario'),
    
    # Respuestas
    path('respuestas/', views.respuestasHome, name='respuestasHome'),
    path('datosPerfil/', views.datosPerfil, name='datosPerfil'),
    path('datosPreguntas/', views.datosPreguntas, name='datosPreguntas'),
    path('datosTextoPreguntas/', views.datosTextoPreguntas, name='datosTextoPreguntas'),
    
    # Preguntas
    path('listarPreguntas/', views.listarPreguntas, name='listarPreguntas'),
    path('modificarPregunta/<id>/', views.modificarPregunta, name='modificarPregunta'),
    path('eliminarPregunta/<id>/', views.eliminarPregunta, name='eliminarPregunta'),
    path('crearPregunta/', views.crearPregunta, name='crearPregunta'),

    # Descargar Excel
    path('descargar_excel/', views.descargar_excel, name='descargar_excel'),
    
    # Mensajes
    path('home_mensajes/', views.homeMensajes, name='mensajesHome'),
    path('crearMensaje/', views.crearMensaje, name='crearMensaje'),
    path('modificarMensaje/<id>/', views.modificarMensaje, name='modificarMensaje'),
    path('eliminarMensaje/<id>/', views.eliminarMensaje, name='eliminarMensaje'),

    # API
    path('apiHome/', apiHome, name='apiHome'),
    path('obtener-id/', ObtenerID.as_view(), name='obtener_id'),    
    path('api_usuario/', UsuarioAPIView.as_view(), name='api_usuario'),
    path('api_pregunta/', UsuarioTextoPreguntaAPIView.as_view(), name='api_pregunta'),
    path('api_respuesta/', UsuarioRespuestaAPIView.as_view(), name='api_respuesta'),
    path('api_mensaje/', MensajeContenidoAPIView.as_view(), name='api_mensaje'),
]