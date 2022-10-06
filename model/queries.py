import sqlite3

con = sqlite3.connect("profile.db")
cur = con.cursor()

class PROFILEque():

    def get_user(self, ctx):
        try:
            cur.execute(f"SELECT * FROM profile_detail WHERE username_id='{ctx}'")
            user_in_db= cur.fetchone();
            return user_in_db

        except sqlite3.Error as error:
            print("error error queries >>", error)