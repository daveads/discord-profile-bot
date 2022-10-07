import sqlite3

#con = sqlite3.connect("profile.db")
#cur = con.cursor()

class PROFILEque():

    def __init__(self):

        self.con = sqlite3.connect("profile.db")
        self.cur = self.con.cursor()


    def get_user(self, ctx):
        try:
            self.cur.execute(f"SELECT * FROM profile_detail WHERE username_id='{ctx}'")
            user_in_db= self.cur.fetchone();
            return user_in_db

        except sqlite3.Error as error:
            print("error error queries >>", error)


    def update(self, table, value, username_id):
        try:
            self.cur.execute(f"UPDATE profile_detail SET {table} ='{value}' WHERE username_id='{username_id}'")

        except sqlite3.Error as error:
            print("unable to update user >>", error)
