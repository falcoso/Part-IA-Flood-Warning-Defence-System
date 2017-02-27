# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:28:40 2017

@author: jones
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    #create list of names stations to be plotted with their measure_id
    highest_levels=stations_highest_rel_level(stations, 5)
    stations_to_plot = []

    for j in highest_levels:
        for i in stations:
            if j[0] == i.name:
                stations_to_plot.append(i)
                       
    dt = 10    
    #plot data for each station
    for i in stations_to_plot:
        
        dates, levels = fetch_measure_levels(i.measure_id,
                                             dt=timedelta(days=dt))
        plot_water_levels(i.name,dates,levels)
    
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    run()