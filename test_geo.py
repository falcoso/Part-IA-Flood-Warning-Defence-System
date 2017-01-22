"""
Created on Sun Jan 22 16:33:01 2017

@author: jones

Unit test for the geo module
"""

import pytest
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, haversine

def test_stations_by_distance():
    
    #build station list
    stations = build_station_list()
    
    p = stations[2].coord    #reference point so that the function is sorted
    
    #check list is output on small sample of stations
    a = stations[0:3]

    #check distances are correct and orderd i.e. stations[2] should be at 
    #testput[0] and their distances equal
    testout = stations_by_distance(a,p)    
    assert haversine(a[2].coord,p) == testout[0][1]
    
