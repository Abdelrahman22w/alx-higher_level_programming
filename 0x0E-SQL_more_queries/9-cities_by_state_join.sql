SELECT cities.id, cities.name, states_.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id;
