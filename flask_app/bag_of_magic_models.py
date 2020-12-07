import numpy as np 
import pandas as pd
from sklearn.decomposition import NMF
import pickle

"""
Data Preprocessing for the movie files:

rating_file = "ratings.csv
Id_file = "movies.csv"

df = pd.read_csv(Id_file)
df.set_index("movieId", inplace=True)
df = df.transpose()

ratings = pd.read_csv(rating_file)
no_users = ratings["userId"].max()

for i in range(no_users):
    df_user = ratings[ratings["userId"]==i].copy().astype(np.float64)
    del df_user["timestamp"]
    del df_user["userId"]
    df_user.set_index("movieId", inplace=True)
    df_user = df_user.transpose()
    df = pd.concat([df,df_user], axis=0)

R = df.copy()
R = R.drop(index=["title","genres"])
"""

R = pd.read_csv("data/reviews.csv")
R.drop(columns=['Unnamed: 0'],inplace=True)

avg_rating = R.mean().mean()
R_imputed = R.fillna(avg_rating)
nmf_model = NMF(n_components=25, max_iter=1500)
nmf_model.fit(R_imputed)
Q = nmf_model.components_
P = nmf_model.transform(R_imputed)
R_hat = pd.DataFrame(np.dot(P, Q), columns=R.columns, index=R.index)
pickle.dump(nmf_model, open("nmf_model.sav", "wb"))