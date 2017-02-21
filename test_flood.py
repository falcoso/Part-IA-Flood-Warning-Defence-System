# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:48:41 2017

@author: Hiral
"""

import pytest
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

#build station list
stations = build_station_list()

def test_stations_level_over_threshold():
    
    for i in stations_level_over_threshold(stations,0.8):
        
        #ensures tuples returned
        assert type(i)==tuple
                   
        #ensures that all the values are above the expected tolerance           
        assert i[1]>0.8          
                   
    