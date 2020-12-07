import pandas as pd

def get_games(number_of_games):
    """
    This function imports the matrix of games/reviews and returns the most
    rated games as a list. The lenght of the list can be specified as
    the parameter number_of_games
    """
        
    df = pd.read_csv("../table.csv", index_col=0)
    
    sorted_games = df.count().sort_values(ascending=False)
    
    most_reviewed_games = list(sorted_games.head(number_of_games).index.values)
    
    return most_reviewed_games
