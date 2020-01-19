# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 13:51:14 2020

@author: csed
"""

import pandas as pd

import topsisarsh.py
    
dataset = pd.read_csv('data.csv')
dataset = dataset.iloc[:,1:].values
print(dataset)
weights = [1,1,1,1]
impact = ["+", "+", "-", "+"]

p = topsisarsh.topsis(dataset,impact,weights)

print(p)
