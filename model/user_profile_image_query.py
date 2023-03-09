import sqlite3

class Imageque():

    def __init__(self):

        self.con = sqlite3.connect("profile.db")
        self.cur = self.con.cursor()

    # user images 
    def get_user_images(self, user_id):
        
        try:
            self.cur.execute(f"SELECT image_name FROM user_profile_images WHERE user_id = {user_id}")
            result = self.cur.fetchall();
            return result

        except sqlite3.Error as error:
            print("error error queries >>", error)


    # total images per user
    def total_user_images(self, user_id):
        try:
            count = self.cur.execute(f"SELECT COUNT(*) FROM user_profile_images WHERE user_id = {user_id};")

            return count.fetchone()[0]

        except sqlite3.Error as error:
            print("error error queries >>", error)