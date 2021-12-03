from  api_recomendacion.models import Calificaciones,UsuariosSr
import   api_recomendacion.Recomendador.calificacionUtilRepo as reco
import api_recomendacion.Recomendador.DatasetUtil as dataSet
import pandas as pd



def listarUsuario():
  usuarios = list(UsuariosSr.objects.values())
  codigo_usuarios=[]
  for i in usuarios:
    codigo_usuarios.append(i.get("cod_usuario"))
  return (codigo_usuarios)

def prueba():
  pass


def indexPeliculas():
  id_peliculas = dataSet.getPandasDataFrame().index.values.tolist()
  return (id_peliculas)




def generarMatrizColaborativa():
  usuarios_ids=listarUsuario()
  peliculas_ids=indexPeliculas()
  usuarioNone=["default"]*len(peliculas_ids)
  df=pd.DataFrame({"default":usuarioNone})
  for cod_usuario in usuarios_ids:
    df[cod_usuario] = df.index.to_series().map(reco.dictCalificaciones(cod_usuario))
  df = df.drop('default', axis=1)
  return df


