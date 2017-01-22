# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 18:06:27 2017

@author: jones
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.utils import sorted_by_key

def run():
    """Requirements for Task 1B"""
    cam_coord = (52.2053,0.1218) #coordinates of Cambridge city centre
    
    #build station list
    stations = build_station_list()
    
    #calculate the distances to coordinates
    distances_to_cam = stations_by_distance(stations, cam_coord)
    
    #10 closest will be the first 10 items in the list
    close10 = distances_to_cam[:10]
    
    #reverse the order and take the first 10 items of the re-orderd list
    distances_to_cam = sorted_by_key(distances_to_cam, 1, reverse=True)
    far10 = distances_to_cam[:10]

    #format outputs
    close10formatted = []
    far10formatted = []
    for i in close10:
        close10formatted.append((i[0].name, i[0].town, i[1]))
    for i in far10:
        far10formatted.append((i[0].name, i[0].town, i[1]))
        
    print("Closest 10 stations to Cambride:")
    for i in close10formatted:
        print(i)
    print("")
    print("Furthest 10 stations from Cambridge:")
    for i in far10formatted:
        print(i)
    
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")

    # Run Task1B
    run()