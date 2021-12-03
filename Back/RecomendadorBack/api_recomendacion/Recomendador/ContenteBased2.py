
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import api_recomendacion.Recomendador.DatasetUtil
import pandas as pd

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
    return self.df.iloc[index_games].to_json(orient='index')

  def devolverJuegosDict(self,index_games):
    return self.df.iloc[index_games].to_dict('index')

  def mappingAndSimilarity(self):
    global mapping,dfm,similarity_matrix,overview_matrix,tfidf
    tfidf = TfidfVectorizer(stop_words="english")
    self.df["Overview"] = self.df["Overview"].fillna("")
    overview_matrix = tfidf.fit_transform(self.df["Overview"])
    similarity_matrix = linear_kernel(overview_matrix,overview_matrix)
    mapping = pd.Series(self.df.index,index = self.df["Name"])

  def recomendarPorJuego(self,index1,cantidad=5):
    global mapping,dfm,similarity_matrix,overview_matrix,tfidf
    game_Index = index1
    similarity_score = list(enumerate(similarity_matrix[game_Index]))
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    similarity_score = similarity_score[1:15]
    index_games = [i[0] for i in similarity_score]
    return index_games

  def recomendarTotalidadJuegos(self):
    self.df=self.df.drop(self.df.index[self.juegosNoGustan])
    self.juegosRecomendados=[]
    self.vectorizarPalabras()
    self.mappingAndSimilarity()
    for i in self.JuegosBase:
      self.juegosRecomendados=[*self.juegosRecomendados,*self.recomendarPorJuego(i)]
    self.juegosRecomendados=list(dict.fromkeys(self.juegosRecomendados))
    return self.devolverJuegosDict(self.juegosRecomendados)





