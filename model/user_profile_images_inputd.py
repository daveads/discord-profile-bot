import sqlite3
from datetime import datetime

con = sqlite3.connect("profile.db")
cur = con.cursor()


class image_data:
    def __init__(self, user_id, image_name):
        self.user_id = user_id
        self.image_name = image_name
        self.uploaded_at = datetime.utcnow().strftime("%d-%m-%Y")

        try:
            cur.execute(
                "INSERT INTO user_profile_images VALUES (NULL, ?, ?, ?)",
                (self.user_id, self.image_name, self.uploaded_at),
            )
            con.commit()

        except sqlite3.Error as error:
            print(f"unable to add image into the database >> ", error)
