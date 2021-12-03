import pandas as pd




def getPandasDataFrame():
  df = pd.read_csv("api_recomendacion/Recomendador/pruebaGeneral.csv",delimiter=";")
  return df


print(getPandasDataFrame())
