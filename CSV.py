'''
Simple code to open a CSV file and print out contents.
The file name is RDS Trns 2.csv and located in what is your current working
directory for that instance of python.
'''

import csv

# open RDS Turns 2.csv and assign to variable file
file = open('RDS Turns 2.csv')

#read the csv file.
fileread = csv.reader(file)

# loops through each row in CSV and print out a tuple of the data
for i in fileread:
    print i

