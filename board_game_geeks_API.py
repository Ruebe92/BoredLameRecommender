import pandas as pd
import requests
import time

#%%

client_id =  "Ip5a9BjpcY"
#client_secret: 9902985c158cf492fda9f32b2cde227c
#redirect_uri: None Set

data_set = []
skip = 0

#%%

date1 = '2018-11-01'
date2 = '2020-11-30'
mydates = pd.date_range(date1, date2).tolist()


#%%

for day in mydates:

    print(day.date())

    date = f"{day.date()}T13:05:37.371Z"

    skip = 0

    for i in range(3):

        request_url = f"https://api.boardgameatlas.com/api/reviews?&client_id=Ip5a9BjpcY&skip={skip}&after_date={date}"

        response = requests.get(request_url)

        data = response.json()['reviews']

        for line in data:

            data_set.append(line)

        skip += 100

        print(f"finished requesting {skip}, start sleeping...")

        time.sleep(1.1)


#%%
df = pd.DataFrame(data_set)
df = df.drop(['id','date','title','description'], axis = 1)

rating_list = []
user_list = []
game_list = []

df_new = pd.DataFrame()

for _, row in df.iterrows():

    rating = row['rating']

    game = row['game']['id']['objectId']

    user = row['user']['username']

    df_new.loc[f'{user}',f'{game}'] = rating


#%%
df_new.to_csv('table.csv')









