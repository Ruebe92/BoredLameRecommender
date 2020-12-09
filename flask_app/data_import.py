import pandas as pd

def get_games(by_category, n_games):
    """
    This function imports the dataframe of most popular games and returns a list of game names
    with the length of 'n_games' selected by 'by_category'. Valid options for 'by_category': rank, num_user_ratings
    """
    df = pd.read_csv('../data/popular_games_with_image_url.csv', index_col = 0)

    if by_category == 'rank':
        ascending = True
    elif by_category == 'num_user_ratings':
        ascending = False

    df = df.sort_values(by_category, ascending = ascending)

    df = df.head(n_games)

    game_list = []
    image_list = []

    for row in df.iterrows():

        #game_name = row[1]['name'] + ' (' + str(row[1]['year_published']) + ')'
        game_name = row[1]['name']
        game_list.append(game_name)

        image_url = row[1]['image_url']
        image_list.append(image_url)



    return game_list, image_list


def get_images_from_game_list(game_list):

    df = pd.read_csv('../data/popular_games_with_image_url.csv', index_col = 0)

    image_list = []
    for game_name in game_list:

        url = df[df['name'] == game_name]['image_url'][0]
        image_list.append(url)

    return image_list





#%%
if __name__ == "__main__":


    games_by_rank = get_games('rank', 15)
    games_by_num_ratings = get_games('num_user_ratings', 15)


