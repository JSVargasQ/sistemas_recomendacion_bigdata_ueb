#
#
# import numpy as np
# import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.metrics import mean_squared_error
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel
# from pandas import read_excel
# import pandas as pd
#
#
# my_sheet = 'respuesta' # change it to your sheet name, you can find your sheet name at the bottom left of your excel file
# file_name = 'prueba.xlsx' # change it to the name of your excel file
# df = read_excel(file_name, sheet_name = my_sheet)
# df = df.set_axis(["title","overview"],axis=1,inplace=False)
# df=df.drop_duplicates(subset=['title'])
#
#
# tfidf = TfidfVectorizer(stop_words="english")
# df["overview"] = df["overview"].fillna("")
# #Construct the required TF-IDF matrix by applying the fit_transform method on the overview feature
# overview_matrix = tfidf.fit_transform(df["overview"])
# similarity_matrix = linear_kernel(overview_matrix,overview_matrix)
# print(similarity_matrix)
#
# #movies index mapping
# mapping = pd.Series(df.index,index = df["title"])
# print(mapping)
#
#
# def recommend_movies_based_on_plot(index1):
#     movie_index = index1
#     print("Buscando relación del videojuego: ")
#     print(df.iloc[index1])
#     #get similarity values with other movies
#     #similarity_score is the list of index and similarity matrix
#     similarity_score = list(enumerate(similarity_matrix[movie_index]))
#     #sort in descending order the similarity score of movie inputted with all the other movies
#     similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
#     # Get the scores of the 15 most similar movies. Ignore the first movie.
#     similarity_score = similarity_score[1:15]
#     #return movie names using the mapping series
#     movie_indices = [i[0] for i in similarity_score]
#     return (df["title"].iloc[movie_indices])
#
# print(df.info)
#
# print(recommend_movies_based_on_plot(57).tolist()[:5])

