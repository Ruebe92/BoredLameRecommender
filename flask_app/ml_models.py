
"""Module for ML Algorithms"""

import json
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity




def nmf_recommender(user_input, no_of_recommendations, path = ""):

    games_to_exclude = user_input.keys()
    to_be_deleted_keys = []
    for key in user_input:
        if isinstance(user_input[key], str):
            to_be_deleted_keys.append(key)
    for key in to_be_deleted_keys:
        del user_input[key]
    
    nmf_model = pickle.load(open(path + "nmf_model.sav", "rb"))
    Id_input = json.load(open(path + "game_ids.json"))

    user_ratings = pd.DataFrame(user_input, index=['Dungeon Master'], columns=Id_input.values())
    user_ratings = user_ratings.fillna(0)
    user_P = nmf_model.transform(user_ratings)
    user_R = pd.DataFrame(np.dot(user_P, nmf_model.components_), index=['Dungeon Master'], columns=Id_input.values())

    recommendations = user_R.drop(columns=games_to_exclude)
    recommendations = recommendations.T.sort_values(by='Dungeon Master', ascending=False)
    output_list = list(recommendations.index[:no_of_recommendations])
    return output_list




def cosim_recommender(user_input, no_of_recommendations, path = ""):
    
    Id_input = json.load(open(path + "game_ids.json"))
    new_user = pd.DataFrame(user_input, index=['Dungeon Master'], columns=Id_input.values()).fillna(0)
    df = pd.read_csv(path + "../data/reviews.csv", index_col=0)
    df = df.append(new_user)
    df = df.fillna(0)
    df = df.T
    unplayed_games = df[df['Dungeon Master'].values == 0].index

    cs_mat = cosine_similarity(df.T)
    cs_mat = pd.DataFrame(cs_mat, columns=df.columns, index=df.columns)
    cs_red = cs_mat['Dungeon Master'].sort_values()
    cs_red = cs_red[-4:-1]
    
    pred_ratings = []
    for game in unplayed_games: 
        nominator = 0
        denominator = 0
        for u in cs_red.index: 
            rating = df[u][df.index == game].values[0]
            sim = cs_mat[u]['Dungeon Master']
            nominator += (sim*rating)
            denominator += sim
        if denominator==0:
            pred_rating=0
        else:
            pred_rating = nominator/denominator
        pred_ratings.append((game, pred_rating))

    recommendations = sorted(pred_ratings, key=lambda tup: tup[1])[-no_of_recommendations:]
    output_list = []
    for k in recommendations:
        output_list.append(k[0])
    output_list = list(reversed(output_list))
    return output_list
    
