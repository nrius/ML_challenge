import numpy as np
import pandas as pd


def mixin_fixer(df):
    ingredients = ['raisins', 'nuts', 'oats', 'chocolate','peanut butter']
    #create columns for each ingredient
    for ingredient in ingredients:
        df[ingredient] = 0
    
    for x in ingredients:
        df[x]=df["mixins"].str.contains(x).astype(float)
    df.drop(["mixins"], axis=1, inplace=True)
    return df