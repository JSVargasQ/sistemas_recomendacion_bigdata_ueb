import pandas as pd

class RecommendationUserUser:

  def __init__(self,matriz:pd.DataFrame,usuarios_ids):
    self.df=matriz
    self.usuarios_ids =usuarios_ids
    self.k=self.usuarios_ids//5
    self.neighbor=None

  def pearsonCorrelation(self):
    self.df_corr = self.df.corr(method='pearson')

  def nearestneighbors(self,corrUser):
    return corrUser[corrUser.index != corrUser.name].nlargest(n=self.k).index.tolist()

  def neighborMethod(self):
    self.neighbor = self.df_corr.apply(lambda col: self.nearestneighbors(col))


