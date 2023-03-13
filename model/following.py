import sqlite3

con = sqlite3.connect("profile.db")
cur = con.cursor()

def main():

  try:
      cur.execute(
        ''' 
        CREATE TABLE following (
        id INTEGER PRIMARY KEY,
        following_id INT NOT NULL, 
        user_id INT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (following_id) REFERENCES users(user_id)
        );

        '''
      )

  except sqlite3.Error as error:
    print("unable to create following table", error)


if __name__ == '__main__':
  main()
