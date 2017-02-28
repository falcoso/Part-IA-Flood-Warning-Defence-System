# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:05:31 2017

@author: jones
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    #create list of names stations to be plotted with their measure_id
    highest_levels=stations_highest_rel_level(stations, 5)
    stations_to_plot = []

    #retrieve the rest of station data for the high
    for j in highest_levels:
        for i in stations:
            if j[0] == i.name:
                stations_to_plot.append(i) 
    
    dt = 5    
    #plot data for each station
    for i in stations_to_plot:
        
        #fetch data for each station
        dates, levels = fetch_measure_levels(i.measure_id,
                                             dt=timedelta(days=dt))
        poly, d0 = polyfit(dates, levels, 4)
        x= matplotlib.dates.date2num(dates)
        
        #plot polynomial
        plt.plot(dates, poly(x - d0), label = "poly fit")
        
        #plot original data 
        plot_water_levels(i.name,dates,levels)
        
        #plot low and high levels
        high_low_ranges = i.typical_range
        low = [high_low_ranges[0]]*len(dates)
        high= [high_low_ranges[1]]*len(dates)
        plt.plot(dates, low, label = "low level")
        plt.plot(dates, high, label = "high level")
        plt.legend(loc='upper left')
        
        #plt.legend("Bestfit", "Original data", "low level", "high level")
        plt.show()
    
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    run()