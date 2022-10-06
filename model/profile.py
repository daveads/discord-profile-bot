import sqlite3
from datetime import datetime
from os.path import exists

con = sqlite3.connect("profile.db")
cur = con.cursor()

def main():
   
  file_exists = exists('profile.db')
  #print(file_exists)

  try:
      cur.execute('''CREATE TABLE IF NOT EXISTS profile_detail (
            id INTEGER PRIMARY KEY ,
            username VARCHAR(255),
            username_id VARCHAR(25),
            name VARCHAR(20),
            location VARCHAR(15),
            height VARCHAR(10),
            dating_status VARCHAR(30),
            looking_for VARCHAR(30),
            hobbies VARCHAR(100),
            biography VARCHAR(150),
            
            premium int,
            premium_day int,
            profile_date VARCHAR(12)
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

      cur.execute("INSERT INTO profile_detail VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (
                                                                  "creator0000",
                                                                  "00000000022331",
                                                                  "daveads", 
                                                                  "internet",
                                                                  "9'10",
                                                                  "single",
                                                                  "a nice lady",
                                                                  "love tinkering and playing with computers",
                                                                  "nothing much yet",
                                                                   
                                                                   0,
                                                                   0,
                                                                  "2022-10-03"))
      print("default values inputed")
      con.commit()

    except sqlite3.Error as error:
      print("unable to input default data >> ", error)

  else:
    print("default data already exist")


if __name__ == '__main__':
  main()

class profile_data():

  def __init__(self, username, username_id, name, location, height, dating_status, looking_for, hobbies, biography ):

    self.username = username
    self.username_id = username_id
    self.name = name
    self.location = location 
    #self.gender = gender #check
    self.height = height
    self.dating_status = dating_status
    self.looking_for = looking_for
    self.hobbies = hobbies
    self.biography = biography
    #self.sexuality = Sexuality
    


    #Defaults
    self.premium = 0 #[0, 1] enum
    self.premium_day = 0
    self.profile_date = datetime.utcnow().strftime("%d-%m-%Y")

    try: 
      cur.execute("INSERT INTO profile_detail VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
      self.username,
      self.username_id,
      self.name,
      self.location,
      self.height,
      self.dating_status,
      self.looking_for,
      self.hobbies,
      self.biography,

      self.premium,
      self.premium_day,

      self.profile_date
    ))
      con.commit()
      con.close()

    except sqlite3.Error as error:
      print(f"unable to create add {self.username} into the database >> ", error)


"""
**removing premium** !needed
"""