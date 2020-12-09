"""Module for ML Algorithms"""

import json
import pandas as pd
import numpy as np
import pickle


def nmf_recommender(user_input, no_of_recommendations):
    games_to_exclude = user_input.keys()
    to_be_deleted_keys = []
    for key in user_input:
        if isinstance(user_input[key], str):
            to_be_deleted_keys.append(key)
    for key in to_be_deleted_keys:
        del user_input[key]
    nmf_model = pickle.load(open("nmf_model.sav", "rb"))
    Id_input = json.load(open("game_ids.json"))
    user_ratings = pd.DataFrame(user_input, index=['DAU'], columns=Id_input.values())
    user_ratings = user_ratings.fillna(0)
    user_P = nmf_model.transform(user_ratings)
    user_R = pd.DataFrame(np.dot(user_P, nmf_model.components_), index=['DAU'], columns=Id_input.values())
    recommendations = user_R.drop(columns=games_to_exclude)
    recommendations = recommendations.T.sort_values(by='DAU', ascending=False)
    output_list = list(recommendations.index[:no_of_recommendations])
    return output_list


def cosim_recommender():
    pass


