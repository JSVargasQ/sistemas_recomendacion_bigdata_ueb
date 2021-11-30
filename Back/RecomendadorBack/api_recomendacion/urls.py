from django.urls import path
from api_recomendacion.views import UsuarioView, CalifacionView, PeliculasView

urlpatterns=[
    path('usuarios/',UsuarioView.as_view(), name='usuario'),
    path('usuarios/<int:cod_usuario>',UsuarioView.as_view(), name='usuario_procesar'),
    path('calificaciones/',CalifacionView.as_view(),name='califiacionesLista'),
    path('peliculas/',PeliculasView.as_view(),name='peliculas')
]
