# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:47:12 2017

@author: jones
"""
import pytest
import numpy as np
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from matplotlib import dates
from datetime import timedelta
from floodsystem.analysis import polyfit

# Build list of stations
stations = build_station_list()
        
# Update latest level data for all stations
update_water_levels(stations)

def test_polyfit():
    
    dt=10
    #create time and level data to be testerd
    times, levels = fetch_measure_levels(stations[0].measure_id, dt=timedelta(days=dt))
    x= dates.date2num(times)
    
    #run polyfit 
    poly, d0 = polyfit(times, levels, 2)
    assert d0 == x[0]
    assert isinstance(poly, np.poly1d)
    
    