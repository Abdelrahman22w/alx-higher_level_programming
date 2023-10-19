-- Create database 'hbtn_0d_2'
-- If database already exists, script should not fail
CREATE DATABASE IF NOT EXIST hbtn_0d_2;

-- Create user 'user_0d_2'
-- User password should be set to 'user_0d_2_pwd'
-- If user already exists, script should not fail
CREATE USER IF NOT EXIST 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- User 'user_0d_2' should have only SELECT privilege in db 'hbtn_0d_2'
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
