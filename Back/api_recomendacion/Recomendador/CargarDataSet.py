import pandas as pd
import re,os



def cargarDatos():
    file = "api_recomendacion/Recomendador/datosJuegos.csv"
    df = pd.read_csv(file, delimiter=";")
    if 'Unnamed: 0' in df:
        df = df.drop('Unnamed: 0', 1)
    print(df.info)
    return ("hola")

