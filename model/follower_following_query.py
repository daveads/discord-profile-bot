import sqlite3


class Following_follower:
    def __init__(self):
        self.con = sqlite3.connect("profile.db")
        self.cur = self.con.cursor()

    # user images
    async def follow_user(self, user_id, follower_id):
        # user_id :: user who is being followed
        # follwer_id :: user who is following

        try:
            self.cur.execute(
                f"INSERT INTO relationship VALUES (NULL, ?, ?)", (user_id, follower_id)
            )

            self.con.commit()

        except sqlite3.Error as error:
            print("error error queries >>", error)

    def unfollower_user(self, user_id, follower_id):
        # user_id  user been unfollowed
        # follower_id user who is unfollowing

        try:
            self.cur.execute(
                f"DELETE FROM relationship WHERE user_id = {user_id} AND follower_id = {follower_id}"
            )

            self.con.commit()

        except sqlite3.Error as error:
            print("error removing the follower ", error)

    def total_followers_count(self, user_id):
        # SELECT COUNT(*) FROM relationship WHERE user_id = <user_id>;
        try:
            count = self.cur.execute(
                f"SELECT COUNT(*) FROM relationship WHERE user_id = {user_id}"
            )
            return count.fetchone()[0]

        except sqlite3.Error as error:
            print("error error queries >>", error)

    def total_following_count(self, user_id):
        try:
            count = self.cur.execute(
                f"SELECT COUNT(*) FROM relationship WHERE follower_id = {user_id};"
            )
            return count.fetchone()[0]

        except sqlite3.Error as error:
            print("error error queries >>", error)

    def followers_list(self, user_id):
        """
        SELECT profile_detail.username_id
        FROM profile_detail
        INNER JOIN relationship ON relationship.follower_id = profile_detail.username_id
        WHERE relationship.user_id = {user_id};
        """

        try:
            """
            self.cur.execute(
                '''SELECT profile_detail.username_id
                 FROM relationship
                 JOIN profile_detail ON relationship.user_id = profile_detail.username_id
                 WHERE relationship.user_id = ?''', (user_id,))
            """

            self.cur.execute(f"SELECT * FROM relationship WHERE user_id = {user_id};")

            result = self.cur.fetchall()

            re = [i[1] for i in result]
            
            return re

        except sqlite3.Error as error:
            print("error error queries >>", error)

    def following_list(self, user_id):
        """
        SELECT profile_detail.username_id
        FROM profile_detail
        INNER JOIN relationship ON relationship.user_id = profile_detail.username_id
        WHERE relationship.follower_id = {follower_id};
        """

        try:
            self.cur.execute(
                f"SELECT * FROM relationship WHERE follower_id = {user_id};"
            )

            result = self.cur.fetchall()

            re = [i[1] for i in result]

            return re

        except sqlite3.Error as error:
            print("error error queries >>", error)

    def user_ff_bool(self, user_id, follower_id):
        try:
            self.cur.execute(
                f"SELECT * FROM relationship WHERE user_id={user_id} AND follower_id={follower_id}"
            )

            result = self.cur.fetchone()
            return result is not None

        except sqlite3.Error as error:
            print("error @ user_follow_bool() queries >>", error)

    # checks if a user is following a particular user
    def user_following_check(self, user_id, following_id):
        try:
            self.cur.execute(
                f"SELECT * FROM relationship WHERE user_id={user_id} AND follower_id={following_id}"
            )

            result = self.cur.fetchone()
            return result is not None

        except sqlite3.Error as error:
            print("error @ user_follow_bool() queries >>", error)
