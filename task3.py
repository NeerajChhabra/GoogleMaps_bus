import csv
import sys
import googlemaps
from datetime import datetime
c=0
d=0
gmaps = googlemaps.Client(key='AIzaSyCxv_9IXZmugxkUEKwQ5-u8Wo7hLe-_2AE')
csv_file = csv.reader(open('Bus_Stops.csv', "rt"))
for row in csv_file:
  try:  
    x=float(row[1])
    y=float(row[0])
  except:
    pass 
  else:
   s_lat=("{:.6f}".format(x))
   s_long=("{:.6f}".format(y))
   origin=(s_lat,s_long)
   for row in csv_file:
     try:  
       x=float(row[1])
       y=float(row[0])
     except:
       pass     
     else:
       d_lat=("{:.6f}".format(x))
       d_long=("{:.6f}".format(y))
       destination=(d_lat,d_long)       
       now = datetime.now()
       directions_result = gmaps.directions(origin,
                                            destination,
                                            mode="transit",
                                            departure_time=now)

     try:
       f = open("output.txt", "a+")
       f.write(directions_result[0]['legs'][0]['distance']['text'])
       f.write("\n")
     except:
       pass
