import sqlite3 as sql
import cv2
import numpy as np
import sys
import time
from PIL import Image

conn = sql.connect('test.db')
c = conn.cursor()

id = int(raw_input('Enter id: '))
name = raw_input('Enter Name: ')
age = int(raw_input('Enter age: '))

#c.execute('CREATE TABLE Facedetails (id int PRIMARY KEY,name text,age int) ')
c.execute("INSERT INTO Facedetails(id,name,age) VALUES(?,?,?)",(id,name,age))
'''
find = raw_input('Enter id to find : ')
c = c.execute("SELECT * FROM Facedetails WHERE id = " + str(find))
for row in c:
    print 'Id = ',row[0]
    print 'name = ',row[1]
    print 'age = ',row[2]
'''
conn.commit()
conn.close()

print "Database Upated Successfully"