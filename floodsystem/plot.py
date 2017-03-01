# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:16:32 2017

@author: jones
"""

import matplotlib
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    """Inputs: station name, dates of data recording and the river levels at that point."
    Outputs: Plot of the water levels against time"""
    
    plt.plot(dates, levels, label = "original data")
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Water levels for {}".format(station))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    
    return

def plot_water_levels_with_fit(station, dates, levels, p):
    """Inputs: station as MonitoringStation class, dates of data recording and the river levels at that point, and the degree of polynomial to be plotted.
    Outputs: Plot of fitted polynomial, original data, and typical ranges"""
    try:
       #fetch data for each station
       poly, d0 = polyfit(dates, levels, 10)
       x= matplotlib.dates.date2num(dates)
        
       #plot polynomial
       plt.plot(dates, poly(x - d0), label = "poly fit")
        
       #plot original data 
       plot_water_levels(station.name,dates,levels)
        
       #plot low and high levels
       high_low_ranges = station.typical_range
       low = [high_low_ranges[0]]*len(dates)
       high= [high_low_ranges[1]]*len(dates)
       plt.plot(dates, low, label = "low level")
       plt.plot(dates, high, label = "high level")
       plt.legend(loc='upper left')
        
       #plt.legend("Bestfit", "Original data", "low level", "high level")
       plt.show()
    
    except:
        print("{} does not have full data available to plot for the given period".format(station.name))