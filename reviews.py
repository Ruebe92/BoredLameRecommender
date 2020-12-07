import pandas as pd
import requests
import time
import feather



def get_dataframe_from(url):

    response = requests.get(request_url)

    time.sleep(1)

    data_raw = response.json()['reviews']

    data_list = []
    for line in data_raw:

        data_list.append(line)

    data_frame = pd.DataFrame(data_list)

    return data_frame

#%% Read and clean data

popular_games = pd.read_csv('popular_games_total.csv')

popular_games = popular_games.sort_values('num_user_ratings',ascending=False)

popular_games_more_than_X =popular_games[popular_games['num_user_ratings'] > 1]

#%%
CLIENT_ID = "Ip5a9BjpcY"
#client_secret: 9902985c158cf492fda9f32b2cde227c
#redirect_uri: None Set

batch_size = 100
old_length = 0

reviews = pd.DataFrame()

game_count = 0

for game_id in popular_games_more_than_X['id']:

    print(game_count)
    game_count += 1
    print(f'game_id: {game_id}')

    for batch in range(9):

        skip = batch * batch_size

        request_url = f'https://api.boardgameatlas.com/api/reviews?pretty=true&client_id={CLIENT_ID}&limit={batch_size}&skip={skip}&game_id={game_id}'

        new_df = get_dataframe_from(request_url)

        reviews = pd.concat([reviews, new_df], axis = 0)

        length_dif = reviews.shape[0] - old_length
        old_length = reviews.shape[0]
        print(old_length)
        if length_dif == 0:
            break

        feather.write_dataframe(reviews, 'reviews.file')


#%%

test = pd.read_feather('reviews.file')
#%%
test = test.drop(['id','date','title','description'], axis = 1)

rating_list = []
user_list = []
game_list = []

df_new = pd.DataFrame()

for _, row in test.iterrows():

    rating = row['rating']

    game = row['game']['id']['objectId']

    user = row['user']['username']

    df_new.loc[f'{user}',f'{game}'] = rating