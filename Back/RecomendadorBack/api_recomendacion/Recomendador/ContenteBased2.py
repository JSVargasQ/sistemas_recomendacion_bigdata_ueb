
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import api_recomendacion.Recomendador.DatasetUtil
import pandas as pd
import json

from api_recomendacion.Recomendador import DatasetUtil


class ContentBaseRecommender:
  def __init__(self):
    self.df=DatasetUtil.getPandasDataFrame()
    self.mapping=""
    self.similarity_matrix=""
    self.tfidf=""
    self.overview_matrix=""
    self.dfm=""
    self.JuegosBase=[]
    self.juegosNoGustan=[]
    self.juegosRecomendados=[]

  def agregarNoGustan(self,index):
    self.juegosNoGustan.append(index)

  def agregarGustan(self,index):
    self.JuegosBase.append(index)

  def vectorizarPalabras(self):
    global mapping,dfm,similarity_matrix,overview_matrix,tfidf
    tfidf = TfidfVectorizer(stop_words="english")
    self.df["Overview"] = self.df["Overview"].fillna("")
    overview_matrix = tfidf.fit_transform(self.df["Overview"])
    similarity_matrix = linear_kernel(overview_matrix,overview_matrix)
    mapping = pd.Series(self.df.index,index = self.df["Name"])

  def devolverListaNombre(self,index_games):
    return (self.df["Name"].iloc[index_games]).tolist()

  def devolverJuegosJson(self,index_games):
    self.df['num']= self.df['referencia']
    return self.df.to_json(orient = 'records')
#    return self.df.reset_index().to_json(orient='records')
  #  json_list = json.loads(json.dumps(list(self.df.iloc[index_games].T.to_dict().values())))
 #   return self.df.to_json(orient = 'records')
#    return self.df.iloc[index_games].to_json(orient='records')

  def devolverJuegosDict(self,index_games):
    if(len(index_games)<1):
      return ("Por el momento no hay mas videojuegos, pronto añadiremos mas")
    self.df['Num'] = self.df['referencia'].astype(str)
    self.df = self.df.drop('referencia', axis=1)
    devolver=self.df.iloc[index_games]
    if(len(devolver.index)>16):
      return self.df.iloc[index_games].sample(16).to_dict('r')

    return self.df.iloc[index_games].to_dict('r')
  def mappingAndSimilarity(self):
    global mapping,dfm,similarity_matrix,overview_matrix,tfidf
    tfidf = TfidfVectorizer(stop_words="english")
    self.df["Overview"] = self.df["Overview"].fillna("")
    overview_matrix = tfidf.fit_transform(self.df["Overview"])
    similarity_matrix = linear_kernel(overview_matrix,overview_matrix)
    mapping = pd.Series(self.df.index,index = self.df["Name"])

  def recomendarPorJuego(self,index1,cantidad=5,):
    global mapping,dfm,similarity_matrix,overview_matrix,tfidf
    game_Index = index1
    similarity_score = list(enumerate(similarity_matrix[game_Index]))
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    similarity_score = similarity_score[1:15]
    index_games = [i[0] for i in similarity_score]
    return index_games

  def organizarIndex(self):
    print((self.df.index))
    self.df['referencia'] = self.df.index
    self.df = self.df.reset_index(drop=True)
    for i in range(len(self.JuegosBase)):
      print("la variable es i ---->", self.JuegosBase[i])
      id_original=self.JuegosBase[i]
      self.JuegosBase[i]=self.df.index[self.df['referencia'] == id_original].tolist()[0]


  def recomendarTotalidadJuegos(self):
    for i in self.JuegosBase:
      if i in self.juegosNoGustan:
        self.juegosNoGustan.remove(i)
    self.df=self.df.drop(self.df.index[self.juegosNoGustan])
    self.organizarIndex()
    self.juegosRecomendados=[]
    self.vectorizarPalabras()
    self.mappingAndSimilarity()
    for i in self.JuegosBase:
      self.juegosRecomendados=[*self.juegosRecomendados,*self.recomendarPorJuego(i)]
    self.juegosRecomendados=list(dict.fromkeys(self.juegosRecomendados))
    return self.devolverJuegosDict(self.juegosRecomendados)





