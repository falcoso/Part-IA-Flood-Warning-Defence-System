# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 19:48:07 2017

@author: jones
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""
    #build station list
    stations = build_station_list()
     
    cam_coord = (52.2053,0.1218) #coordinates of Cambridge city centre
    
    #create list of stations within 10km
    stations_within_10 = stations_within_radius(stations, cam_coord, 10)
    
    #create list of just station names
    names_within_10 = []
    for i in stations_within_10:
        names_within_10.append(i[0].name)
     
    #order the list
    names_within_10.sort
    
    print("Stations within 10km of Cambridge")
    for i in names_within_10:
        print(i)
    
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")

    # Run Task1C
    run()