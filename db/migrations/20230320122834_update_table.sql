-- migrate:up

ALTER TABLE profile_detail DROP COLUMN premium_days;
ALTER TABLE profile_detail DROP COLUMN premium_exp_date;
ALTER TABLE profile_detail ADD age INTEGER(10);

CREATE TABLE IF NOT EXISTS user(
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

insert into user SELECT id, username, username_id, name, location, looking_for, hobbies, biography, age, profile_date FROM profile_detail;


DROP table profile_detail;
ALTER TABLE user RENAME TO profile_detail;

-- migrate:down

