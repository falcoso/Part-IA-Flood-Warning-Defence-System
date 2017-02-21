# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:48:41 2017

@author: Hiral
"""

import pytest
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold,stations_highest_rel_level

#build station list
stations = build_station_list()
update_water_levels(stations)

def test_stations_level_over_threshold():
    
    for i in stations_level_over_threshold(stations,0.8):
        
        #ensures tuples returned
        assert type(i)==tuple
                   
        #ensures that all the values are above the expected tolerance           
        assert i[1]>0.8  

def test_stations_highest_rel_level():
    
    highest_levels=stations_highest_rel_level(stations, 10)
    
    #ensure that the function returns a list of the correct length
    assert len(highest_levels)==10
                

                   
    