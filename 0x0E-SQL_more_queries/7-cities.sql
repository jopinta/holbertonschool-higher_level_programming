-- cities snafran with FK
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
id INT PRIMARY KEY, state_id INT FOREIGN KEY, name VARCHAR(256) NOT NULL);
