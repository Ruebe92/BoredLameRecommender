# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:56:24 2020

@author: chris
"""

import pandas as pd

popular_games = pd.read_csv('popular_games.csv')

popular_games = popular_games.drop('Unnamed: 0', axis = 1)
#%%
popular_games.to_csv('popular_games_with_image_url', index = False)