-- Display the score and name of records where the name
-- is not NULL or empty, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
