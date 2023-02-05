CREATE USER 'fly_fishing'@'localhost' IDENTIFIED BY 'fly_fishing_pass';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES,
RELOAD on *.* TO 'fly_fishing'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
CREATE DATABASE IF NOT EXISTS fly_fishing_store_info;