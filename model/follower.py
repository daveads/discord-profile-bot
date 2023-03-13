import sqlite3

con = sqlite3.connect("profile.db")
cur = con.cursor()

def main():

  try:
      cur.execute(
        ''' 
        CREATE TABLE followers (
        id INTEGER PRIMARY KEY,
        follower_id INT NOT NULL,
        user_id INT NOT NULL,
        FOREIGN KEY (follower_id) REFERENCES users(user_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
        '''
      )

  except sqlite3.Error as error:
    print("unable to create followers table", error)


if __name__ == '__main__':
  main()
