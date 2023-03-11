"""
Create followers table

CREATE TABLE followers (
  follower_id INT,
  user_id INT,
  FOREIGN KEY (follower_id) REFERENCES users(user_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

"""