import pandas as pd

def structure_ratings(dictionary, user_name):
    """ 
    This function extracts the data from the user input, 
    and returns it as a dataframe.
    """
    
    df = pd.DataFrame()
    
    for index in range(1,int(1+len(dictionary)/2)):
        
        rating = dictionary[f'rating{index}']
        
        game = dictionary[f'game{index}']
        
        df.loc['user_name',game] = rating
        
    return df