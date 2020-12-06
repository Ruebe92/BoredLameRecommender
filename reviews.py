import pandas as pd
import requests
import time



def get_dataframe_from(url):

    response = requests.get(request_url)

    time.sleep(1)

    data_raw = response.json()
    data_list = []

    for line in data_raw['games']:

        new_line = [line['id'], line['name'], line['rank'], line['year_published'], line['num_user_ratings']]

        data_list.append(new_line)

    data_frame = pd.DataFrame(data_list, columns = ['id','name', 'rank', 'year_published','num_user_ratings'])

    return data_frame

#%%

CLIENT_ID = "Ip5a9BjpcY"
#client_secret: 9902985c158cf492fda9f32b2cde227c
#redirect_uri: None Set

popular_games = pd.read_csv('popular_games_total.csv')

request_url = f'https://api.boardgameatlas.com/api/reviews?pretty=true&client_id={CLIENT_ID}?game_id=TAAifFP590'

response = requests.get(request_url)

data_raw = response.json()