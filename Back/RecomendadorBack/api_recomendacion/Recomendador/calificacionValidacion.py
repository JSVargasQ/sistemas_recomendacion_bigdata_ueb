

from api_recomendacion.models import Calificaciones

def buscarCalificacionPorUsuario(cod_usuario):
   return Calificaciones.objects.raw('Select * from calificaciones where cod_usuario = %s',[cod_usuario])


def calificacionBuenasXusuario(cod_usuario):
  return Calificaciones.objects.raw('Select * from calificaciones where puntuacion = 1 and cod_usuario = %s', [cod_usuario])
