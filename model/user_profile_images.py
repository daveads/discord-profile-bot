import sqlite3

con = sqlite3.connect("profile.db")
cur = con.cursor()

def main():

  try:
    #TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      cur.execute(
        ''' 
        CREATE TABLE IF NOT EXISTS user_profile_images (
        id INTEGER PRIMARY KEY,
        user_id VARCHAR(25) NOT NULL,
        image_name VARCHAR(255) NOT NULL,
        uploaded_at VARCHAR(20),
        FOREIGN KEY (user_id) REFERENCES profile_detail(username_id))
        
      '''
      )

      #print("Table created")

  except sqlite3.Error as error:
    print("unable to create database table", error)


if __name__ == '__main__':
  main()
