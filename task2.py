import csv
import sys
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCxv_9IXZmugxkUEKwQ5-u8Wo7hLe-_2AE')

source=input("Enter the Source bus stop number = ")


def get_lat_long(stop):
  csv_file = csv.reader(open('Bus_Stops.csv', "rt"))
  for row in csv_file:
    if stop == row[4]:
       x=float(row[1])
       y=float(row[0])
       lat=("{:.6f}".format(x))
       long=("{:.6f}".format(y))
       li=[lat,long]
       return(li)
      
s_li=get_lat_long(source)
s_lat=s_li[0]
s_long=s_li[1]

dest=input("Enter the destination bus stop number = ")

d_li=get_lat_long(dest)
d_lat=s_li[0]
d_long=s_li[1]

reverse_geocode_result_org=(s_lat, s_long)
reverse_geocode_result_dest=(d_lat, d_long)

now = datetime.now()
directions_result = gmaps.directions(reverse_geocode_result_org,
                                     reverse_geocode_result_dest,
                                     mode="transit",
                                     departure_time=now)

print("The distance to be travelled is : ",directions_result[0]['legs'][0]['distance']['text'])
