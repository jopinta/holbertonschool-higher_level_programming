-- list cities in DB
SHOW DATABASE hbtn_0d_usa.cities.id;
SHOW DATABASE hbtn_0d_usa.cities.name;
SHOW DATABASE hbtn_0d_usa.states.name;
SELECT cities FROM hbtn_0d_usa
JOIN states on cities.state_id=states.id ORDER BY cities.id;