-- This script lists all the cities of
-- carlifonia that can be found in the database
SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY cities.id 
