"""Module for ML Algorithms"""

# TO-DO: Get movies from file or from database

from faker import Faker
import json
import pandas as pd
import numpy as np
import pickle

def simple_recommender(num):
    fake = Faker()
    fake_names = [fake.name() for i in range(num)]
    return fake_names


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


if __name__ == "__main__":
    user_input = json.load(open("user2_input.json"))
    test_recommendation = nmf_recommender(user_input,5)
    print(test_recommendation)