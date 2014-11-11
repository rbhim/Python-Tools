# -*- coding: utf-8 -*-
"""
Created on Sun Nov 09 21:44:54 2014

@author: RBhim
"""

import sqlite3
conn = sqlite3.connect("traffic1.sqlite") #connect or create traffic db
curs = conn.cursor()

curs.execute("""DROP TABLE IF EXISTS traffic""")#drop table if it exist

#Create Table traffic with three columns Speed:Flow:LOS
f = curs.execute("""CREATE TABLE traffic(Speed INT,
                                         Flow INT,
                                         LOS STRING)""")
#Create a list of tuples. Remember tubles are ordered dataset so ideal for db
Data = [
        (40,400,"A"),
        (40,500,"B"),
        (50,600,"C"),
        (50,700,"C"),
        (60,800,"D"),
        (80,800,"D"),
        (90,1000,"E"),
        (100,2000,"F")
        ]
#Insert many fiels as once. You can use the curs.execute to insert only onw row
curs.executemany("INSERT INTO traffic VALUES (?,?,?)", Data)

#Saving changes to traffic db
conn.commit()    

conn.close()
