import pandas as pd
import requests
import time


CLIENT_ID = "Ip5a9BjpcY"
#client_secret: 9902985c158cf492fda9f32b2cde227c
#redirect_uri: None Set


def get_dataframe_from(url):

    response = requests.get(request_url)

    time.sleep(1)

    data_raw = response.json()
    data_list = []

    for line in data_raw['games']:

        new_line = [line['id'], line['name'], line['rank'], line['year_published'], line['num_user_ratings'], line['image_url']]

        data_list.append(new_line)

    data_frame = pd.DataFrame(data_list, columns = ['id','name', 'rank', 'year_published','num_user_ratings', 'image_url'])

    return data_frame



popular_games = pd.DataFrame()
batch_size = 100
old_length = 0

for year in range(1950, 2021):

    print(f'Year: {year}')

    for batch in range(9):

        skip = batch * batch_size

        request_url = f'https://api.boardgameatlas.com/api/search?&year_published={year}&client_id={CLIENT_ID}&order_by=popularity&limit={batch_size}&skip={skip}'

        new_df = get_dataframe_from(request_url)

        popular_games = pd.concat([popular_games, new_df], axis = 0)

        length_dif = popular_games.shape[0] - old_length
        old_length = popular_games.shape[0]
        print(old_length)
        if length_dif == 0:
            break



#%%
popular_games =  popular_games.sort_values('rank')

popular_games.drop_duplicates(subset=['id'])

popular_games.to_csv('popular_games.csv')









