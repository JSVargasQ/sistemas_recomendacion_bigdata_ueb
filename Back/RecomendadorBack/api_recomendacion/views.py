from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from api_recomendacion.Recomendador import CargarDataSet

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
            cali = list(Calificaciones.objects.filter(cod_usuario=cod_usuario).values())
            if (len(cali) > 0):
                response = {'Calificación': cali,
                            'message': 'Success'}
            else:
                response = {
                    'message': 'No hay calificaciones'}
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
