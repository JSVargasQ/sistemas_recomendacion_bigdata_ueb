

from api_recomendacion.models import Calificaciones

def buscarCalificacionPorUsuario(cod_usuario):
   return Calificaciones.objects.raw('Select * from calificaciones where cod_usuario = %s',[cod_usuario])


buscarCalificacionPorUsuario(1)
