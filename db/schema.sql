CREATE TABLE user_profile_images (
        id INTEGER PRIMARY KEY,
        user_id VARCHAR(25) NOT NULL,
        image_name VARCHAR(255) NOT NULL,
        uploaded_at VARCHAR(20),
        FOREIGN KEY (user_id) REFERENCES profile_detail(username_id));
CREATE TABLE relationship (
        relationship_id INTEGER PRIMARY KEY,
        user_id VARCHAR(25) NOT NULL,
        follower_id VARCHAR(25) NOT NULL,
        FOREIGN KEY (user_id) REFERENCES profile_detail(username_id),
        FOREIGN KEY (follower_id) REFERENCES profile_detail(username_id)
        );
CREATE TABLE IF NOT EXISTS "schema_migrations" (version varchar(255) primary key);
CREATE TABLE IF NOT EXISTS "profile_detail"(
		    id INTEGER PRIMARY KEY,
            username VARCHAR(255),
            username_id VARCHAR(25),
            name VARCHAR(20),
            location VARCHAR(15),
            looking_for VARCHAR(30),
            hobbies VARCHAR(100),
            biography VARCHAR(150),
			age INTEGER(10),
            profile_date VARCHAR(12)
);
-- Dbmate schema migrations
INSERT INTO "schema_migrations" (version) VALUES
  ('20230320122834');
