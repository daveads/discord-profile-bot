import sqlite3
from datetime import datetime

datenow = datetime.now()

datenow.strftime("%d/%m/%Y %H:%M")

con = sqlite3.connect("profile.db")
cur = con.cursor()

from os.path import exists
file_exists = exists('profile.db')
#print(file_exists)

try:
    cur.execute('''CREATE TABLE IF NOT EXISTS profile_detail (
            id INTEGER PRIMARY KEY ,
            username VARCHAR(255),
            name VARCHAR(20),
            location VARCHAR(15),
            hobbies VARCHAR(100),
            biography VARCHAR(150),
            height VARCHAR(10),
            Searching_for VARCHAR(30),
            Sex VARCHAR(10),
            premium_day int,
            Profile_date VARCHAR(12),
            premium int
            )''')
    #print("Table created")
except sqlite3.Error as error:
  print("unable to create database table", error)



test = cur.execute("SELECT * FROM profile_detail WHERE ROWID IN ( SELECT max( ROWID ) FROM profile_detail );")
test0 = ()
for i in test:
    test0 = i


if len(test0) == 0:
  try:
    cur.execute("INSERT INTO profile_detail VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (1,
                                                                  "creator0000", 
                                                                  "daveads", 
                                                                  "internet", 
                                                                  "hobby is playing with computers",
                                                                  "none",
                                                                  "Tall",
                                                                  "a nice lady",
                                                                  "male",
                                                                  1,
                                                                  "2022-10-03",
                                                                  0))
    print("default values inputed")
    con.commit()

  except sqlite3.Error as error:
    print("unable to create default table", error)

else:
  print("default data already exist")



class profile_data():
  pass