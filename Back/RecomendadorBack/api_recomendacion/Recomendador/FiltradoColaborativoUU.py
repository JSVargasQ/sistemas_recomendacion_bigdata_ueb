import csv
from math import sqrt

import pandas as pd
import numpy as np
from django.http import JsonResponse

from scipy.stats import pearsonr

from api_recomendacion.models import Calificaciones


def descargarBdCalificaciones():
  calificacion = list(Calificaciones.objects.values())
  if (len(calificacion) > 0):
    myFile = ('api_recomendacion/Recomendador/datosBD.csv')
    #df = pd.DataFrame(calificacion)
    #df.to_csv(myFile)
  leerCsv()

  data = ''

def processCol(col):
  return col.astype(str).apply(lambda val: val.replace(',', '.')).astype(float)

def leerCsv():
  data = pd.read_csv('api_recomendacion/Recomendador/datosBD.csv', dtype=object)
  data = data.apply(processCol)
  df_corr = data.corr(method='pearson')
  vecinos = df_corr.apply(lambda col: vecinosCercanos(col))

  prediccionPelicula = data.apply(
    lambda ratings: calcularRecomendacionUser(vecinos[ratings.name],
                                              df_corr[ratings.name][vecinos[ratings.name]],
                                              data))

  print(prediccionPelicula['1'].sort_values(ascending=False).head(2))



def vecinosCercanos(corrUser, k=5):
  return corrUser[corrUser.index != corrUser.name].nlargest(n=k).index.tolist()

def calcularRecomendacionUser(vecinosCercanos, usercorr, data):
  def calcularPrediccionPelicula(vecinosCercanos, usercorr, ratingPelicula):
    tieneCalificacion = ~np.isnan(ratingPelicula)
    if (np.sum(tieneCalificacion) != 0):
      return np.dot(ratingPelicula.loc[tieneCalificacion], usercorr.loc[tieneCalificacion]) / np.sum(
        usercorr[tieneCalificacion])
    else:
      return np.nan
  return data.apply(lambda fila: calcularPrediccionPelicula(vecinosCercanos, usercorr, fila[vecinosCercanos]), axis=1)
