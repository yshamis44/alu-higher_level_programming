-- Lists the score and the name of the rows of second_table with a score >= 10, best score first.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
