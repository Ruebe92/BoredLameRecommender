import numpy as np 
import pandas as pd 
import pickle
import json

nmf_model = pickle.load(open("nmf_model.sav", "rb"))

def recommend_me_nmf(user_input, no_of_recommendations):
    Id_input = json.load(open("flask_app/game_ids.json"))
    user_ratings = pd.DataFrame(user_input, index=['DAU'], columns=Id_input.values())
    user_ratings = user_ratings.fillna(0)
    user_P = nmf_model.transform(user_ratings)
    user_R = pd.DataFrame(np.dot(user_P, nmf_model.components_), index=['DAU'], columns=Id_input.values())
    print(user_R)
    recommendations = user_R.drop(columns=user_input.keys())
    recommendations = recommendations.T.sort_values(by='DAU', ascending=False)
    return recommendations.iloc[:no_of_recommendations]

def recommend_me_cosim(user_input, no_of_recommendations):
    pass

def recommend_me_cluster(user_input, no_of_recommendations):
    pass

if __name__ == "__main__":
    user_input = json.load(open("flask_app/user3_input.json"))
  
    recommendations = recommend_me_nmf(user_input, 7)
    print(recommendations)