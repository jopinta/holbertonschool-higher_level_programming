-- creatins server user
CREATE USER [IF NOT EXISTS] 'user_0d_1'@'localhost'
IDENTIFIED BY 'pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
