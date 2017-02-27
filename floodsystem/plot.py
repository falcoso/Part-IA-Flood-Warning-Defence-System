# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:16:32 2017

@author: jones
"""

import matplotlib
import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    "Inputs: station name, dates of data recording and the river levels at that point."
    "Outputs: Plot of the water levels against time"
    
    plt.plot(dates, levels)
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Water levels for {}".format(station))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()
    
    
    