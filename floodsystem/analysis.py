# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:38:21 2017

@author: jones
"""

import numpy as np
import matplotlib

def polyfit(dates, levels, p):
    """Inputs: List of dates and the corresponding water levels, and the degree of polynomial p
    Output: Plot of fit polynomial and original data"""
    
    x= matplotlib.dates.date2num(dates)
    
    #define offset
    d0 = x[0]
    
    #create coefficients for function
    p_coeff = np.polyfit(x - d0, levels, p)
    
    #define polynomial function
    poly = np.poly1d(p_coeff)

    return poly, d0