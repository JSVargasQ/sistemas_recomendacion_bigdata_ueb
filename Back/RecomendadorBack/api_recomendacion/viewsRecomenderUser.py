from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import api_recomendacion.Recomendador.calificacionUtilRepo   as caliUtil
from api_recomendacion.Recomendador import CargarDataSet, FiltradoColaborativoUU
from  api_recomendacion.Recomendador.ContenteBased2 import ContentBaseRecommender
from api_recomendacion.modelsDTO.models import CalificacionesDTO
from api_recomendacion.Respository import  GeneralRepository
import json

from api_recomendacion.models import UsuariosSr, Calificaciones



class ContenidoUsuarioUsuario(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self,request,cod_usuario=0):
      matriz=GeneralRepository.generarMatrizColaborativa()

      return JsonResponse({"hola":cod_usuario})

    def post(self, request):
      jd = json.loads(request.body)
      cod_usuario=jd.get("usuario")
      clase=ContentBaseRecommender()
      listCalifaciones = []

      # Se guardan las selecciones del usuario
      for juego in jd.get("juegos"):
        listCalifaciones.append(CalificacionesDTO(cod_usuario,juego.get("Num"),juego.get("Puntuacion")))
      caliUtil.juegosCalificados(cod_usuario,listCalifaciones)
      resultadoGustar=caliUtil.CalificacionesGustanPorUsuario(jd.get("usuario"))
      resultadoNoGustar=caliUtil.CalificacionesNoGustanPorUsuario(jd.get("usuario"))

      # se agregan las que se califican mal en la clase de recomendación para que no entren el las recomendaciones
      for calificaMal in resultadoNoGustar:
        clase.agregarNoGustan(calificaMal.cod_videojuego)
      # se agregan las calificaciones que el usuario ha calificado como buenas
      for calificaciones in resultadoGustar:
        clase.agregarGustan(calificaciones.cod_videojuego)

      #se ejecuta el recomendador por contenido del usuario de acuerdo a lo que le gusta y lo que no le gusta
      #print(clase.recomendarTotalidadJuegos())

      #se ejecuta el recomendador por contenido del usuario de acuerdo a lo que le gusta y lo que no le gusta
      #print(clase.recomendarTotalidadJuegos())
      return JsonResponse(clase.recomendarTotalidadJuegos())



