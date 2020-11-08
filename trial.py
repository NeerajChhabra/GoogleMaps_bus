import csv

stop=input("Enter the stop number = ")
fin=csv.reader(open('Bus_Stops.csv','rt'))
for row in fin:
	print(row)    
 
