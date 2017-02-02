
"""
Created on Thu Feb  2 17:22:44 2017

@author: Hiral
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    
    #build station list
    stations=build_station_list()
    
    #creates sorted set of rivers monitored
    rivers_monitored=rivers_with_station(stations)
    
    #prints the first 10 entries in the set
    print(rivers_monitored[0:10])
    
    #generates dictionary
    stations_by_river_dict=stations_by_river(stations)
    
    #prints dictionary entries for 3 rivers
    print("\n",stations_by_river_dict['River Aire'])
    print("\n",stations_by_river_dict['River Cam'])
    print("\n",stations_by_river_dict['Thames'])
    
    
    
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")

    # Run Task1D
    run()


    