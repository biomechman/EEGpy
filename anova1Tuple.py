# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:53:00 2017
@author: biomechman

"""
from scipy import stats

def anova1Tuple(data):
    ''' Computes F-values in a tuple array
    Input: paired arrays of data to be compared. 
    Output: blahblahblah
    '''
    
    F, p = stats.f_oneway(data['grp1'], data['grp2'], data['grp3']);
   
    ''' Degrees of Freedom '''
    dfBetween = k - 1;
    dfWithin = N - k;
    dfTotal = N - 1;
    
    ''' Sum of Squares & Mean Squares'''
    ssBetween = ((sum(data.groupby('grp3').sum()['grp2']) ** 2) / n) - ((data['grp2'].sum() ** 2) / N);
    sumYsquared = sum([value ** 2 for value in data['grp2'].values]);
    ssWithin = sumYsquared - (sum(data.groupby('grp3').sum()['grp2'] ** 2) / n);
    ssTotal = sumYsquared - ((data['grp2'].sum() ** 2) / N);
    msBetween = ssBetween / dfBetween;
    msWithin = ssWithin / dfWithin;
    
    F = 