import sqlite3
from datetime import datetime

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
            looking_for VARCHAR(30),
            dating_status VARCHAR(30),

            premium_day int,
            profile_date VARCHAR(12),
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

    cur.execute("INSERT INTO profile_detail VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (
                                                                  "creator0000", 
                                                                  "daveads", 
                                                                  "internet",
                                                                  "love tinkering and playing with computers",
                                                                  "nothing much yet",
                                                                  "9'10",
                                                                  "a nice lady",
                                                                  "single",
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

  def __init__(self, username, name, location, hobbies, biography, height, looking_for, dating_status):

    self.username = username
    self.name = name
    self.location = location 
    #self.gender = gender #check
    self.hobbies = hobbies
    self.biography = biography
    self.height = height
    self.looking_for = looking_for
    #self.sexcuality = Sexuality
    self.dating_status = dating_status


    #Defaults
    self.premium = 0 #[0, 1] enum
    self.premium_day = 0
    self.profile_date = datetime.utcnow().strftime("%d-%m-%Y")

    cur.execute("INSERT INTO confession VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
      self.username,
      self.name,
      self.location,
      self.hobbies,
      self.biography,
      self.height,
      self.looking_for,
      self.dating_status,

      self.premium,
      self.premium_day,
      
      self.profile_date
    ))
    con.commit()