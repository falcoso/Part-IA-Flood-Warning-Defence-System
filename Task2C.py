# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:11:12 2017

@author: Hiral
"""
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    highest_levels=stations_highest_rel_level(stations, 10)
    
    for i in highest_levels:
        print(i[0],i[1])


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    run()