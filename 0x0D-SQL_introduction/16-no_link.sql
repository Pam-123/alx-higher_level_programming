-- Script to list all records with non-empty name values, ordered by descending score
USE `hbtn_0c_0`;

SELECT score, name
FROM `second_table`
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
