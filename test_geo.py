"""
Created on Sun Jan 22 16:33:01 2017

@author: jones

Unit test for the geo module
"""

import pytest
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, haversine, stations_within_radius

#build station list
stations = build_station_list()

#create test variables    
testpoint = stations[2].coord    #reference point so that the function is sorted
teststations = stations[0:3]   #take small sample of stations

#testout results are tested first before being re-used in the second test
testout = stations_by_distance(teststations,testpoint)  

def test_stations_by_distance():
    
    #check distances are correct and orderd i.e. stations[2] should be at 
    #testput[0] and their distances equal  
    assert haversine(teststations[2].coord,testpoint) == testout[0][1]

def test_stations_within_radius():
    
    #find a value of r that take only the first 2 items by sorting the 
    #distances and taking the second one
    a = []
    for i in testout:
        a.append(i[1])
        
    a.sort
    
    #checking that the length of the output is correct length and that the 
    #items are in range order
    testout2 = stations_within_radius(teststations,testpoint,a[1])
    assert len(testout2) == 2
    assert testout2[0][1] < testout2[1][1]
    