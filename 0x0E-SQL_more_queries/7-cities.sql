-- Create db 'hbtn_0d_usa'
-- If db already exists, script should not fail
CREATE DATABASE IF NOT EXIST hbtn_0d_usa

-- Create table 'cities' in db 'hbtn_0d_usa'
-- id INT unique, auto generated, not null, primary key
-- state_id INT not null, foreign key that references id of 'states' table
-- name VARCHAR(256) not null
-- If table already exists, script should not fail
CREATE TABLE IF NOT EXIST hbtn_0d_usa.cities(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL FOREIGN KEY REFERENCE TO hbtn_0d_usa.states(id),
    name VARCHAR(256) NOT NULL
);
