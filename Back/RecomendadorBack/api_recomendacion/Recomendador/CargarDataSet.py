import pandas as pd
import csv
import json


def cargarDatos():
  file = "api_recomendacion/Recomendador/DatasetFinal.csv"
  df = pd.read_csv(file,sep=';', error_bad_lines=False, index_col=0)
  c =df.to_csv('api_recomendacion/Recomendador/datosJuegosFinal.csv')
  c = df.sample(10)
  c.to_csv('api_recomendacion/Recomendador/datosJuegosNuevos.csv')
  csv_to_json('api_recomendacion/Recomendador/datosJuegosNuevos.csv')
  f = open("api_recomendacion/Recomendador/datosJuegos.json", "r")
  content = f.read()
  jsondecoded = json.loads(content)

  return jsondecoded

def csv_to_json(file):
  jsonArray = []
  csvFilePath = file
  jsonFilePath = 'api_recomendacion/Recomendador/datosJuegos.json'
  # read csv file
  with open(csvFilePath, encoding='utf-8') as csvf:
    # load csv file data using csv library's dictionary reader
    csvReader = csv.DictReader(csvf)

    # convert each csv row into python dict
    for row in csvReader:
      # add this python dict to json array
      jsonArray.append(row)

  # convert python jsonArray to JSON String and write to file
  with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    jsonString = json.dumps(jsonArray, indent=4)
    jsonf.write(jsonString)


