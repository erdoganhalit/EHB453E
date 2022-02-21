# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import numpy as np
import googlemaps
import json
gmaps = googlemaps.Client(key='AIzaSyBJ4FOD2JU5Nn4H7UcyD8nmCfJPJtXVFwE')
f = open(r'C:\Users\halit.erdogan\coordinates.json')
# returns JSON object as a dictionary
data = json.load(f)
for dictTemp in data:
    originTemp = dictTemp['firstLoc']
    origin_latitude = originTemp[0]
    origin_longitude = originTemp[1]

    destTemp = dictTemp['destLoc']
    destination_latitude = destTemp[0]
    destination_longitude = destTemp[1]

    distance = gmaps.distance_matrix([str(origin_latitude) + " " + str(origin_longitude)], [str(destination_latitude) + " " + str(destination_longitude)],
                                     mode='driving')['rows'][0]['elements'][0]
    value = distance['distance']['value']
    dictTemp['distance'] = distance
with open("coordinate_distance.json", "w") as final:
    json.dump(data, final)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
