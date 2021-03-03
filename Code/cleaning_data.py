#functions 

import pandas as pd
import numpy as np

#nurias version: do not drop density, keep values under 2.
#remove weight under 0
#log transform sugar to flour

def dropping_rows_and_columns(df):
    '''
    dropping diameter becuase it has no sdt dev, all values are the same
    drop rows with nans in column mixins
    dropping chill time, because it is highly correlated with calories
    '''
    df.drop(columns="diameter", inplace=True)
    df.dropna(how='any', subset=['mixins'], inplace=True)
    df.drop(columns="chill time", inplace=True)
    df.drop(columns=["aesthetic appeal", "crunch factor", "density"], inplace=True)
    df.drop(df[df["calories"] < 0].index, inplace=True) 
    df.drop(df[df["weight"] < 0].index, inplace=True)
    df.drop(df[df["grams baking soda"] > 1.2].index, inplace=True)
    df.drop(df[df["sugar to flour ratio"] > 1].index, inplace=True)
    
    
    # converting sugar index to numpy
    sugar_index = np.array(df["sugar index"])
    #log transform sugar index
    df["sugar index"] = np.log(sugar_index)
    
   
    #the same for bake temp
    bake_temp = np.array(df["bake temp"])
    df["bake temp"] = np.log(bake_temp)
    
    return df