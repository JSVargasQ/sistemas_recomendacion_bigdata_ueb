import pandas as pd
import numpy as np

class RecommendationUserUser:

  def __init__(self,matriz:pd.DataFrame,cantidad_usuarios,user):
    self.df=matriz
    self.usuarios_ids =cantidad_usuarios
    self.k=self.usuarios_ids//5
    self.neighbor=None
    self.user_id=user

  def pearsonCorrelation(self):
    self.df_corr = self.df.corr(method='pearson')

  def nearestneighbors(self,corrUser):
    return corrUser[corrUser.index != corrUser.name].nlargest(n=self.k).index.tolist()

  def neighborMethod(self):
    self.neighbor = self.df_corr.apply(lambda col: self.nearestneighbors(col))

  def calcularRecomendacionUser(predictvideojuego, nearNeig, usercorr, data):
    def predecirVideojuego(vecinosCercanos, usercorr, ratingVideoGame):
      tieneCalificacion = ~np.isnan(ratingVideoGame)
      if (np.sum(tieneCalificacion) != 0):
        return np.dot(ratingVideoGame.loc[tieneCalificacion], usercorr.loc[tieneCalificacion]) / np.sum(
          usercorr[tieneCalificacion])
      else:
        return np.nan

    return data.apply(lambda fila: predecirVideojuego(nearNeig, usercorr, fila[nearNeig]), axis=1)

  def predecirJuegosPorUsuario(self):
    self.pearsonCorrelation()
    self.neighborMethod()
    prediccionVideoJuego = self.df.apply(lambda ratings: self.calcularRecomendacionUser(self.neighbor[ratings.name], self.df_corr[ratings.name][self.neighbor[ratings.name]], self.df))
    print(prediccionVideoJuego[prediccionVideoJuego > -1])
    return (prediccionVideoJuego[self.user_id].sort_values(ascending=False)[:10].to_dict())
