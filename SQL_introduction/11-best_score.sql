-- Lists all records of the table with a score >= 10 second_table
-- Records are ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
