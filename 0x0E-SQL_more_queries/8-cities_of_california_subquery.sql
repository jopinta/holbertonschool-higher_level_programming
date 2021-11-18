-- listing CALI cities from DB subquery
SELECT DISTINCT id, name FROM cities
WHERE state_id=(SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id;
