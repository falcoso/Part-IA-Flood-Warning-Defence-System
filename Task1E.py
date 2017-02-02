
"""
Created on Thu Feb  2 18:42:09 2017

@author: Hiral
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    
    #build station list
    stations=build_station_list()
    
    #N=int(input('Enter a number of rivers' ))
    N=9
    
    #runs function
    print(rivers_by_station_number(stations,N))

    
    

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")

    # Run Task1E
    run()
