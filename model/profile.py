import sqlite3
from datetime import datetime
from os.path import exists

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

con = sqlite3.connect("profile.db")
cur = con.cursor()


def main():
    file_exists = exists("profile.db")
    # print(file_exists)

    try:
        cur.execute(
            """CREATE TABLE IF NOT EXISTS profile_detail (
            id INTEGER PRIMARY KEY ,
            username VARCHAR(255),
            username_id VARCHAR(25),
            name VARCHAR(20),
            location VARCHAR(15),
            looking_for VARCHAR(30),
            hobbies VARCHAR(100),
            age INTEGER(10),
            biography VARCHAR(150),
            profile_date VARCHAR(12)
            )"""
        )

        # print("Table created")

    except sqlite3.Error as error:
        print("unable to create database table", error)

    test = cur.execute(
        "SELECT * FROM profile_detail WHERE ROWID IN ( SELECT max( ROWID ) FROM profile_detail );"
    )
    test0 = ()
    for i in test:
        test0 = i

    if len(test0) == 0:
        try:
            cur.execute(
                "INSERT INTO profile_detail VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                (
                    "creator0000",
                    "00000000022331",
                    "daveads",
                    "internet",
                    "a nice lady",
                    "love tinkering and playing with computers",
                    "500",
                    "nothing much yet",
                    "2022-10-03",
                ),
            )
            print("default values inputed")
            con.commit()

        except sqlite3.Error as error:
            print("unable to input default data >> ", error)

    else:
        logger.info(f'Default data already exist')


if __name__ == "__main__":
    main()


class profile_data:
    def __init__(
        self, username, username_id, name, location, looking_for, hobbies, age, biography
    ):
        self.username = username
        self.username_id = username_id
        self.name = name
        self.location = location
        # self.gender = gender #check
        self.looking_for = looking_for
        self.hobbies = hobbies
        self.age = age
        self.biography = biography
    
        # self.sexuality = Sexuality
        # height
        # relationship status

        self.profile_date = datetime.utcnow().strftime("%d-%m-%Y")

        try:
            cur.execute(
                "INSERT INTO profile_detail VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    self.username,
                    self.username_id,
                    self.name,
                    self.location,
                    self.looking_for,
                    self.hobbies,
                    self.age,
                    self.biography,
                    self.profile_date,
                ),
            )
            con.commit()
            # con.close()

        except sqlite3.Error as error:
            print(f"unable to create add {self.username} into the database >> ", error)


"""
**removing premium** !needed
"""
