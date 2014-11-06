'''
Simple code to connect to SQLite db, reads and print out rows.
The file name is RDS.sqlite and located in what is your current working
directory for that instance of python.
'''

import sqlite3
conn = sqlite3.connect('RDS.sqlite')
cursor = conn.cursor()
f = cursor.execute("Select * FROM RDS")
for i in f:
    print i
    

