import pandas as pd




def getPandasDataFrame():
  df = pd.read_csv("pruebaGeneral.csv",delimiter=";")
  df = df.drop('Unnamed: 0', axis=1)
  return df


print(getPandasDataFrame())
