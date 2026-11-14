-- Lists all the cities of California, using a subquery and no JOIN.
-- Select the cities whose state_id is the id of California.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
