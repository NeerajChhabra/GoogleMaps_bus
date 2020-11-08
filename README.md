# Inwk6312-GoogleMap API Take home
# Programming Task 5

  - You have to clone this repo to your account, you should be seeing this on your account, if someone elses name is listed call an instructor for help.
  - Use the Ubuntu VM to write the progrm.
  - Use git add, commit and push to send the code back. 
  - Don't forget to add user name and email on git. 
  - Read the API
  - Submission in 2 days

# Halifax Open Data

You are given a csv file from [Halifax's open data](https://www.halifax.ca/home/open-data). 

  - The file is a csv (comma seperated values); i.e, it's like a excel spreadsheet but simple
  - You can read the file without modification to it.
  - You are asked to extract some information from it. 

# Google Maps

Read more at https://github.com/googlemaps/google-maps-services-python


### Bus Stop

The CSV you are given has details of the Point representation of bus stop locations which occur along roadways, terminals and park and ride facilities in HRM. Includes information on the type of bus stop and stop number.  This is a point dataset that has been derived from the source data in Hastus (Halifax Transit system).

This is the origianl source  -> https://catalogue-hrm.opendata.arcgis.com/datasets/bus-stops


## Create a different python file for each task with the format task#.py (where # = task number!)

### Task - 1

Create a virtual environment called "gmapdemo" and install google maps api inside it. 
https://docs.python.org/3/tutorial/venv.html

Create a file called task1.py inside the venv that does the following:


```py
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='Add Your Key here')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
```

Just print the resulting results on the screen.

### Task - 2

Notice that bus_stop have x and y co-ordinates for each stop. Look at the google distance matrix API https://developers.google.com/maps/documentation/distance-matrix/
This is API for distance between two co-ordiantes in different units  https://developers.google.com/maps/documentation/distance-matrix/intro#unit_systems

Your task is to find the distance between any two stops in the bus_stops in kms, based on input from the user.

Write a function to get 2 "Stop Number" from the user and return the distance between them.

### Task - 3

Find the distance between all the stops in the given csv and create a distance matrix [https://en.wikipedia.org/wiki/Distance_matrix, https://en.wikipedia.org/wiki/Euclidean_distance_matrix]

Use an appropriate data structure for this task or use a file if you run out of memory.  
Bonus: Redo task 2, with task 3.

License
----
MIT
https://www.halifax.ca/home/open-data/open-data-license


### assignment accepted
