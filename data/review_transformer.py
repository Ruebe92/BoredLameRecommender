# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:00:46 2020

@author: chris
"""

import pandas as pd

#%%

popular_games = pd.read_csv('/data/popular_games_total.csv')

popular_games = popular_games.sort_values('num_user_ratings',ascending=False)

popular_games_more_than_X =popular_games[popular_games['num_user_ratings'] > 1]

#%%

df = pd.read_feather('reviews.file')

df = df.drop(['id','date','title','description'], axis = 1)
#%%
rating_list = []
user_list = []
game_list = []

df_new = pd.DataFrame()

for _, row in df.iterrows():

    rating = row['rating']

    game_id = row['game']['id']['objectId']

    game_object = popular_games_more_than_X[popular_games_more_than_X['id'] == game_id]

    game_name = game_object['name'].iloc[0]

    user = row['user']['username']

    df_new.loc[f'{user}',f'{game_name}'] = rating


#%%

df_new.to_csv('reviews.csv')