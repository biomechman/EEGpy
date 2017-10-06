# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:53:00 2017
@author: biomechman

"""
from scipy import stats
import numpy as np

def anova1Tuple(data):
    ''' Computes F-values in a tuple array
    Input: paired arrays of data to be compared. 
    Output: blahblahblah
    '''
    
    k = len(data);
    n0 = len(data[0])    
    n1 = len(data[1])
    N = n0 + n1
    g0 = np.array(data[0])
    g1 = np.array(data[1])    
    
    
    ''' Degrees of Freedom '''
    dfBetween = k - 1;
    dfWithin = N - k;
    dfTotal = N - 1;
    
    ''' Sum of Squares & Mean Squares'''
    X = (sum(g0)+sum(g1))/N    
    ssTotal = sum((g0 - X)**2) + sum((g1 - X)** 2)
    ssWithin = sum((g0 - sum(g0)/n0)**2) + sum((g1 - sum(g1)/n1)**2)
    ssBetween = ssTotal - ssWithin
    msBetween = ssBetween/dfBetween
    msWithin = ssWithin / dfWithin
  
    ''' F-value, p-value, eta-squared & omega-squared '''  
    F = msBetween / msWithin
    F, p = stats.f_oneway(g0, g1) ''' <<-- Gotta test this stuff... '''
    etaSqrd = ssBetween/ssTotal
    omegaSqrd = (ssBetween - (dfBetween * msWithin)) / (ssTotal + msWithin)
    
    return F,p,etaSqrd,omegaSqrd,ssBetween,ssWithin,ssTotal,dfBetween,dfWithin,dfTotal
 
[F,p,etaSqrd,omegaSqrd,ssBetween,ssWithin,ssTotal,dfBetween,dfWithin,dfTotal] = anova1Tuple(data)   