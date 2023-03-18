import sqlite3

con = sqlite3.connect("profile.db")
cur = con.cursor()


def main():
    try:
        cur.execute(
            """ 
        CREATE TABLE IF NOT EXISTS relationship (
        relationship_id INTEGER PRIMARY KEY,
        user_id VARCHAR(25) NOT NULL,
        follower_id VARCHAR(25) NOT NULL,
        FOREIGN KEY (user_id) REFERENCES profile_detail(username_id),
        FOREIGN KEY (follower_id) REFERENCES profile_detail(username_id)
        );

        """
        )

    except sqlite3.Error as error:
        print("unable to create relationship table", error)


if __name__ == "__main__":
    main()


# single relationship table  vs follower following table
# one way relationship vs mutual relationship
