

from api_recomendacion.models import Calificaciones

def buscarCalificacionPorUsuario(cod_usuario):
   return Calificaciones.objects.raw('Select * from calificaciones where cod_usuario = %s',[cod_usuario])


def devolverCodigosGusto(cod_usuario):
  respuesta=[]
  for i in Calificaciones.objects.raw('Select * from calificaciones where cod_usuario = %s and puntuacion = %s',[cod_usuario,1]):
    respuesta.append(i.cod_videojuego)
  return respuesta

def CalificacionesNoGustanPorUsuario(cod_usuario):
  return Calificaciones.objects.raw('Select * from calificaciones where cod_usuario = %s and puntuacion = %s',[cod_usuario,-1])


def CalificacionesGustanPorUsuario(cod_usuario):
  return Calificaciones.objects.raw('Select * from calificaciones where cod_usuario = %s and puntuacion = %s',[cod_usuario,1])

def dictCalificaciones(cod_usuario):
  id_juegosCalificados={}

  for calificacionesUsuario in buscarCalificacionPorUsuario(cod_usuario):
    juego=calificacionesUsuario.cod_videojuego
    id_juegosCalificados[juego]=calificacionesUsuario.puntuacion
  return id_juegosCalificados

def juegosCalificados(cod_usuario,CalificacionesGuardar:list):
  id_juegosCalificados={}

  for calificacionesUsuario in buscarCalificacionPorUsuario(cod_usuario):
    juego=calificacionesUsuario.cod_videojuego
    id_juegosCalificados[juego]=calificacionesUsuario.cod_calificacion
  listaCalificada=(list(id_juegosCalificados.keys()))

  for i in CalificacionesGuardar:
    if( int(i.cod_videojuego) in listaCalificada):
      cod_calificacion=id_juegosCalificados.get(int(i.cod_videojuego))
      calificacionEncontrada=getCalificacion(cod_calificacion)
      calificacionEncontrada.puntuacion=i.puntuacion
      calificacionEncontrada.save()
    else:
      guardarCalificacionUsuario(i)


def getCalificacion(cod_calificacion)->Calificaciones:
  calificacion = (Calificaciones.objects.get(cod_calificacion=cod_calificacion))
  return calificacion


def guardarCalificacionUsuario(i:Calificaciones):
  calificacion = Calificaciones.objects.create(
  cod_usuario=i.cod_usuario,
  cod_videojuego=i.cod_videojuego,
  puntuacion=i.puntuacion
  )
