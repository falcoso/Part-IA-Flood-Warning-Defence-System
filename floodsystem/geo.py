"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from math import radians, cos, sin, asin, sqrt

AVG_EARTH_RADIUS = 6371  # in km

def haversine(point1, point2, miles=False):
    """ Calculate the great-circle distance between two points on the Earth surface.
    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.
    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))
    :output: Returns the distance bewteen the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True.
    """
    # unpack latitude/longitude
    lat1, lng1 = point1
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
    h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))
    if miles:
        return h * 0.621371  # in miles
    else:
        return h  # in kilometers

    
def stations_by_distance(stations,p):
    """Inputs - stations: list of stations with data type MonitoringStation
    p: tuple containing the coordinates of a point.
    
    Output - a list of tuples containing the stations and their distances from 
    point p sorted in order of those distances. Distances are calculated using
    the haversine function"""
    
    distances = [] #initialise result variable  
    
    #for each station calulcate the distance to p and store
    for station in stations:
        distances.append((station,haversine(station.coord,p)))
     
    #sort the array produced
    sorted_distances = sorted_by_key(distances,1)
    return sorted_distances

def stations_within_radius(stations, centre, r):
    """Inputs - stations: list of stations with data type MonitoringStation
    centre: tuple of coordinates from which the radius is measured
    r: desired radius
    
    Output - list of all stations (data type MonitoringStation) within radius r
    of centre"""
    
    #find the distances of each station from centre
    distances = stations_by_distance(stations, centre)
    
    #test distance with radius and put into new list
    within_radius=[]
    for i in distances:
        if i[1] <= r:
            within_radius.append(i)
            
    return within_radius

def rivers_with_station(stations):
    """Inputs - stations:list of stations with data type MonitoringStation
    
    Output - returns all stations with a monitoring station"""
    
    #creates list
    list_of_rivers_monitored=[]
    
    #iterates through the stations and appends the river that they monitor to the set
    for station in stations:
        list_of_rivers_monitored.append((station.river))
    
    #turns the list into a set and sorts it alphabetically
    rivers_monitored=sorted(set(list_of_rivers_monitored))
    
    return rivers_monitored

def stations_by_river(stations):
    
    """Inputs - stations:list of stations with data type MonitoringStation
    Output - returns dictionary of all stations that monitor the river"""
    
    stations_by_river_dict={}
    
    for station in stations:
        if station.river in stations_by_river_dict.keys():
            stations_by_river_dict.get(station.river).append(station.name)
            stations_by_river_dict.get(station.river).sort()
            
        else:
            stations_by_river_dict[station.river]=[station.name]
            
    return(stations_by_river_dict)
            
    


       
    
    
    
        
    