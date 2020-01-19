# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 13:35:25 2020

@author: csed
"""
import pandas as pd
import math


def topsis(dataset, impacts, weights):
    sumrootsq = []
    numRows= len(dataset)
    numCols= len(dataset[1])
    
    #Creating Normalised Decision Matrix
    for i in range(0, numRows):
        sumr = 0;
        for j in range(0, numCols):
            sumr = sumr + (dataset[i,j]*dataset[i,j]) 
        sumr=math.sqrt(sumr)
        sumrootsq.append(sumr)

    for i in range(0, numRows):
        for j in range(numCols):
            dataset[i,j]=dataset[i,j]/sumrootsq[i]
   
    #Multiplying Columns by weights
    for i in range(0, numRows):
        for j in range(0, numCols):
            dataset[i,j]=dataset[i,j]*weights[j]
            
    #Calculating Ideal Values for each column
    positive = []
    negative = []
    for i in range(0, numCols):
        min = 10000000
        max = -10000000
        for j in range(0, numRows):
            if dataset[j, i]> max:
                max = dataset[j,i]
            if dataset[j, i]<min:
                min = dataset[j,i]
        if impacts[i]=='+':
            positive.append(max)
            negative.append(min)
        elif impacts[i]=='-':
            positive.append(min)
            negative.append(max)
    
    #Caluclating Euclidean Distance from ideal values
    spositive = []
    snegative = []
    for i in range(0, numRows):
        splus = 0
        sminus = 0
        for j in range(0, numCols):
            splus = splus + (dataset[i,j]-positive[j])*(dataset[i,j]-positive[j])
            sminus = sminus + (dataset[i,j]-negative[j])*(dataset[i,j]-negative[j])
        splus = math.sqrt(splus)
        sminus = math.sqrt(sminus)
        spositive.append(splus)
        snegative.append(sminus)
    
    #Calculating Rating    
    rating = []
    for i in range(0,len(spositive)):
        rating.append(snegative[i]/(spositive[i]+snegative[i]))

    return rating
    
    


    
        