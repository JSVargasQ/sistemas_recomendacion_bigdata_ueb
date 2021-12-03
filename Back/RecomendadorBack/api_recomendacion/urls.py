from django.urls import path
from api_recomendacion.views import UsuarioView, CalifacionView, PeliculasView, calificacionesBDView, loginView

urlpatterns=[
    path('usuarios/',UsuarioView.as_view(), name='usuario'),
    path('usuarios/<int:cod_usuario>',UsuarioView.as_view(), name='usuario_procesar'),
    path('calificaciones/',CalifacionView.as_view(),name='califiacionesLista'),
    path('peliculas/',PeliculasView.as_view(),name='peliculas'),
    path('bd/', calificacionesBDView.as_view(), name='bd'),
    path('login/', loginView.as_view(), name='bd')
]
