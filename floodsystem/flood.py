# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:30:39 2017

@author: Hiral
"""

def stations_level_over_threshold(stations, tol):
    """Input - station list and tolerance level
    Output - a list of the stations with relative water levels above the tolerance level"""
    
    stations_over_threshold=[]
    
    for station in stations:
        if type(station.relative_water_level())==float and station.relative_water_level() > tol:
            stations_over_threshold.append((station.name,station.relative_water_level()))
    stations_over_threshold=sorted(stations_over_threshold,key=lambda x:x[1],reverse=True)
    
    return(stations_over_threshold)