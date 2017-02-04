# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 21:27:53 2017

@author: Hiral
"""
from floodsystem.stationdata import build_station_list
from floodsystem.geo import inconsistent_typical_range_stations

def run():
    
    #creates list of stations
    stations=build_station_list()
    inconsistent_list = sorted(inconsistent_typical_range_stations(stations))
    
    print("\n","Stations with inconsistent level data:")    
    #prints the list returned by the function
    for i in inconsistent_list:
        print(i)  


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")

    # Run Task1F
    run()