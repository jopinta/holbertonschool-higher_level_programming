-- computes the score average of all records
SELECT COUNT(score) - COUNT(DISTINCT score)
FROM second_table;
