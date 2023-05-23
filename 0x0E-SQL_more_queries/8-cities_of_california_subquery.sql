-- This script lists all the cities of
-- carlifonia that can be found in the database
SELECT id, name
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id 
