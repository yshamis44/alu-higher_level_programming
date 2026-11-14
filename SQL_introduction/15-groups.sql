-- Lists the number of rows for each score, the most common score first.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
