-- This script lists out all the 
-- cities contained and their 
-- corresponding state names
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states
ON cities.state_id = states.id
