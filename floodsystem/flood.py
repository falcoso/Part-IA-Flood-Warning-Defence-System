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

def stations_highest_rel_level(stations, N):
    """Input - station list and number of stations to return
    Output - a list of the N stations most at risk with their relative levels"""
    
    stations_and_levels=[]

    
    for station in stations:
        if type(station.relative_water_level())==float:
            stations_and_levels.append((station.name,station.relative_water_level()))
    stations_and_levels=sorted(stations_and_levels,key=lambda x:x[1],reverse=True)
    
    return(stations_and_levels[0:N])
    
    