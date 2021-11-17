-- data base name passed as argument
CREATE TABLE IF NOT EXIST second_table AS
select [id INT, name VARCHAR(256), score INT ]
FROM hbtn_0c_0
