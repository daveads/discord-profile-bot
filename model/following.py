"""
CREATE TABLE followings (
  user_id INT,
  following_id INT,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (following_id) REFERENCES users(user_id)
);

"""