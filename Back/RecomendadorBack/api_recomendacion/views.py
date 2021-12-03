from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
<<<<<<< Updated upstream
<<<<<<< Updated upstream
import api_recomendacion.Recomendador.calificacionValidacion   as caliUtil
from api_recomendacion.Recomendador import CargarDataSet, BasadoContenido, FiltradoColaborativoUU, DatasetUtil

=======
=======
>>>>>>> Stashed changes
import api_recomendacion.Recomendador.calificacionUtilRepo   as caliUtil
from api_recomendacion.Recomendador import CargarDataSet, FiltradoColaborativoUU
from  api_recomendacion.Recomendador.ContenteBased2 import ContentBaseRecommender
from api_recomendacion.modelsDTO.models import CalificacionesDTO
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
from django.urls import reverse
import json

from api_recomendacion.models import UsuariosSr, Calificaciones


class UsuarioView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request,cod_usuario=0):
        if(cod_usuario==0):
            usuarios= list(UsuariosSr.objects.values())
            if(len(usuarios)>0):
                response= {'usuarios':usuarios,
                           'status':'Success'}
            else:
                response= {
                           'status':'No hay usuarios'}
            return JsonResponse(response)
        else:
            usuario=list(UsuariosSr.objects.filter(cod_usuario=cod_usuario).values())
            if(len(usuario)>0):
                usuario=usuario[0]

                response= {'usuario':usuario,
                           'status':'Success'}
            else:
                response= {'status':'No existe usuario'}
            return JsonResponse(response)

    def post(self,request):
        jd=json.loads(request.body)
        usuario = list(UsuariosSr.objects.filter(correo=jd['correo']).values())
        if (len(usuario) == 0):
            usuarioAgregar=UsuariosSr.objects.create(
                nombre_usuario = jd['nombre_usuario'],
                pais = jd['pais'],
                fecha_nacimiento = jd['fecha_nacimiento'],
                    correo = jd['correo'],
                password = jd['password'],
            )
            response = {'cod_usuario': usuarioAgregar.cod_usuario ,
                        'status': 'Success'}
        else:
            response = {'status': 'Usuario ya registrado'}
        return JsonResponse(response)

    def put(self, request):
        jd = json.loads(request.body)
        usuario = list(UsuariosSr.objects.filter(cod_usuario=jd['cod_usuario']).values())
        if (len(usuario) > 0):
            usuarioModificar=UsuariosSr.objects.get(cod_usuario=jd['cod_usuario'])
            usuarioModificar.nombre_usuario=jd['nombre_usuario']
            usuarioModificar.pais=jd['pais']
            usuarioModificar.fecha_nacimiento=jd['fecha_nacimiento']
            usuarioModificar.password=jd['password']
            usuarioModificar.save()

            response = {'actualizar':"Se ha Actualizado" ,
                        'status': 'Success'}
        else:
            response = {'status': 'No existe ese usuario'}
        return JsonResponse(response)

class PeliculasView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self,request):
        datos=CargarDataSet.cargarDatos()
        response = {'message': datos}
        return JsonResponse(response)

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
<<<<<<< Updated upstream

      #se ejecuta el recomendador por contenido del usuario de acuerdo a lo que le gusta y lo que no le gusta
      #print(clase.recomendarTotalidadJuegos())


=======

      #se ejecuta el recomendador por contenido del usuario de acuerdo a lo que le gusta y lo que no le gusta
      #print(clase.recomendarTotalidadJuegos())


>>>>>>> Stashed changes
      return JsonResponse(clase.recomendarTotalidadJuegos())
    """  nombresJuegos = jd['juegos']
      array = []
      for i in nombresJuegos:
        array.append(i)
      rta = BasadoContenido.generarRecomendacion(array)
      js = CargarDataSet.devolverInformacionRecomendacion(rta)
      """


class calificacionesBDView(View):
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def get(self, request):
    FiltradoColaborativoUU.descargarBdCalificaciones()
    response = {'message': 'sucess'}
    return JsonResponse(response)



class loginView(View):
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def post(self, request):
    jd = json.loads(request.body)
    usuarioList = list(UsuariosSr.objects.filter(correo=jd['correo']).values())
    if (len(usuarioList) > 0):
      usuario = UsuariosSr.objects.get(correo=jd['correo'])
      if(usuario.password == jd['password']):
        response = {'cod_usuario': usuario.cod_usuario,
                  'status': 'Success'}
      else:
        response = {'status': 'Nombre de usuario o contraseña incorrecto'}
    else:
      response = {'status': 'Nombre de usuario o contraseña incorrecto'}

    return JsonResponse(response)


class CalifacionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, cod_usuario=0):
      #buscar por codigo de calificacion
        if (cod_usuario == 0):
            calificacion = list(Calificaciones.objects.values())
            if (len(calificacion) > 0):
                response = {'Calificación': calificacion,
                            'message': 'Success'}
            else:
                response = {
                    'message': 'No hay calificaciones'}
            return JsonResponse(response)
        else:
            calificacion = caliUtil.calificacionBuenasXusuario(cod_usuario)
            dic=[]
            cs = DatasetUtil.getPandasDataFrame()
            for f in calificacion:
              nom = cs[cs['Num'] == f.cod_videojuego]['Name']
              nom = nom.to_json()
              dic.append({'cod_videojuego':f.cod_videojuego, 'puntuacion':f.puntuacion, 'nombre': nom})

            j = json.dumps(dic)
            response = {'Calificación': j,
                        'message': 'Success'}
            return JsonResponse(response)

    def post(self, request):
        jd = json.loads(request.body)
        calificacion = Calificaciones.objects.create(
            cod_usuario=jd['cod_usuario'],
            cod_videojuego=jd['cod_videojuego'],
            puntuacion=jd['puntuacion']
        )
        response = {
            'message': 'Se ha agregado correctamente',
            'cod_calificacion': calificacion.cod_calificacion
        }
        return JsonResponse(response)


class RecomendacionContenido(View):

      def post(self,request):
        jd = json.loads(request.body)

        resultado = caliUtil.buscarCalificacionPorUsuario(jd.get("usuario"))
        for calificaciones in resultado:
          print("el videojuego Calificado es ", calificaciones.cod_videojuego)
          print("La calificación es ", calificaciones.puntuacion)
        for juego in jd.get("juegos"):
          print(juego)

        return JsonResponse({"hola": "xd"})

      """  nombresJuegos = jd['juegos']
        array = []
        for i in nombresJuegos:
          array.append(i)
        rta = BasadoContenido.generarRecomendacion(array)
        js = CargarDataSet.devolverInformacionRecomendacion(rta)
        """
