import pandas as pd

def structure_ratings(dictionary, user_name):
    """ 
    This function extracts the data from the user input, 
    and returns it as a pandas DataFrame.
    """
    
    df = pd.DataFrame()
    
    for key,val in dictionary.items():
        
        df.loc[f'{user_name}',key] = val
        
    return df
