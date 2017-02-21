# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:11:12 2017

@author: Hiral
"""
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    stations_over_threshold=stations_level_over_threshold(stations,0.8)
    
    for i in stations_over_threshold:
        print(i[0],i[1])


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    run()