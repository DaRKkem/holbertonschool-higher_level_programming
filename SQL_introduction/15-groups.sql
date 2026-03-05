-- Display each score with the number of records
-- having that score, ordered by count descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
