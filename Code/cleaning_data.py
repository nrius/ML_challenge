#functions 

import pandas as pd

def dropping_rows_and_columns(df):
    '''
    dropping diameter becuase it has no sdt dev, all values are the same
    drop rows with nans in column mixins
    dropping chill time, because it is highly correlated with calories
    '''
    df.drop(columns="diameter", inplace=True)
    df.dropna(how='any', subset=['mixins'], inplace=True)
    df.drop(columns="chill time", inplace=True)
    return df