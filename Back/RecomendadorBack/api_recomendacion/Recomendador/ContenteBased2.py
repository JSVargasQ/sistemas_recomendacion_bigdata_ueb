
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import DatasetUtil
import pandas as pd

df=DatasetUtil.getPandasDataFrame()
mapping=""
similarity_matrix=""
tfidf=""
overview_matrix=""
dfm=""

def vectorizarPalabras():
  global mapping,dfm,similarity_matrix,overview_matrix,tfidf
  tfidf = TfidfVectorizer(stop_words="english")
  df["Overview"] = df["Overview"].fillna("")
  overview_matrix = tfidf.fit_transform(df["Overview"])
  similarity_matrix = linear_kernel(overview_matrix,overview_matrix)
  mapping = pd.Series(df.index,index = df["Name"])

def mappingAndSimilarity():
  global mapping,dfm,similarity_matrix,overview_matrix,tfidf
  tfidf = TfidfVectorizer(stop_words="english")
  df["Overview"] = df["Overview"].fillna("")
  #Construct the required TF-IDF matrix by applying the fit_transform method on the overview feature
  overview_matrix = tfidf.fit_transform(df["Overview"])
  similarity_matrix = linear_kernel(overview_matrix,overview_matrix)
  mapping = pd.Series(df.index,index = df["Name"])

def recomendarPorJuego(index1,cantidad=5):
  vectorizarPalabras()
  mappingAndSimilarity()
  global mapping,dfm,similarity_matrix,overview_matrix,tfidf
  game_Index = index1
  print(similarity_matrix)
  similarity_score = list(enumerate(similarity_matrix[game_Index]))
  similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
  similarity_score = similarity_score[1:15]
  index_games = [i[0] for i in similarity_score]
  return (df["Name"].iloc[index_games]).tolist()[:cantidad]


print(recomendarPorJuego(57))
