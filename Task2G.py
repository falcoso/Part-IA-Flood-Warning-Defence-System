# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:30:16 2017

@author: jones
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit
from matplotlib import dates

def run():
    # Build list of stations
    stations = build_station_list()
        
    # Update latest level data for all stations
    update_water_levels(stations)
    
    #create list of names stations to be plotted with their measure_id
    highest_levels=stations_highest_rel_level(stations, 60)
    stations_to_check = []

    #retrieve the rest of station data for the high
    for j in highest_levels:
        for i in stations:
            if j[0] == i.name:
                stations_to_check.append(i) 
    
    #time period for plot
    dt=2
    polydegree = 10

    severe = []
    high = []
    low = []
    moderate = []
    rating_store = [low, moderate, high, severe]
    ratings  = ['severe','high','moderate','low']

    for i in stations_to_check:
        category = 0
        
        #if there is no value for relative water level, we need to check the rest of the data anyway so set it to greater than 1
        if i.relative_water_level() is None:
            rel_level = 2
        else:
            rel_level = i.relative_water_level()
            
        #check to see if level is above average
        if rel_level > 1:
            category =+ 2
        #fetch data for each station
        times, levels = fetch_measure_levels(i.measure_id, dt=timedelta(days=dt))
        x= dates.date2num(times)
            
        #create polyfit for stations
        if len(times) != 0:
            poly, d0 = polyfit(times,levels, polydegree)
            trend = poly.deriv()
        
            if trend(x[0]-d0) > 0:
                category =+ 1
                
        rating_store[category].append(i.town)
        
    for i in range(len(ratings)):
        print("\n", "The following Towns have a {} warning:".format(ratings[i]))
        for j in rating_store[len(ratings)-i -1]:
            print(j)
   
    return
    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")

    run()