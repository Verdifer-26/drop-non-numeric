# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv('isre.csv') #import data
cols = ['column_1', 'column_2'] #declare colukns to be used
dfnum = (df.drop(cols, axis=1).join(df[cols].apply(pd.to_numeric, errors='coerce'))) #change non numeric to NaN
dfnum[dfnum[cols].notnull().all(axis=1)]
clean = dfnum[dfnum[cols].notnull().all(axis=1)] #save data into a new dataframe dropping columns with NaN

clean.to_csv('numberonly.csv', index = False)
