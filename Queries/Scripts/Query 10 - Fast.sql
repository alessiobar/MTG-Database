ALTER TABLE sets ADD prevSet varchar(50);
ALTER TABLE sets ADD nextSet varchar(50);
# ALTER TABLE sets DROP prevSet;
# ALTER TABLE sets DROP nextSet;

WITH temp_prev AS (SELECT s1.name AS currSet, s2.name AS prevSet, s2.releaseDate AS prevReleaseDate
	FROM sets s1 LEFT JOIN sets s2 ON (s1.releaseDate > s2.releaseDate OR (s1.releaseDate = s2.releaseDate AND s1.name > s2.name))),
    temp_next AS (SELECT s1.name AS currSet, s2.name AS nextSet, s2.releaseDate AS nextReleaseDate
	FROM sets s1 LEFT JOIN sets s2 ON (s1.releaseDate < s2.releaseDate OR (s1.releaseDate = s2.releaseDate AND s1.name < s2.name)))

UPDATE sets s
SET s.prevSet = (SELECT prev_table.prevSet
	FROM (SELECT temp_prev1.currSet, max(temp_prev1.prevSet) AS prevSet, temp_prev1.prevReleaseDate AS prevReleaseDate
		FROM temp_prev AS temp_prev1
		WHERE (temp_prev1.currSet, temp_prev1.prevReleaseDate) in (SELECT temp_prev0.currSet, max(temp_prev0.prevReleaseDate)
			FROM temp_prev AS temp_prev0
			GROUP BY temp_prev0.currSet) OR temp_prev1.prevReleaseDate IS NULL
		GROUP BY temp_prev1.currSet) AS prev_table
    WHERE s.name = prev_table.currSet
);

WITH temp_prev AS (SELECT s1.name AS currSet, s2.name AS prevSet, s2.releaseDate AS prevReleaseDate
	FROM sets s1 LEFT JOIN sets s2 ON (s1.releaseDate > s2.releaseDate OR (s1.releaseDate = s2.releaseDate AND s1.name > s2.name))),
    temp_next AS (SELECT s1.name AS currSet, s2.name AS nextSet, s2.releaseDate AS nextReleaseDate
	FROM sets s1 LEFT JOIN sets s2 ON (s1.releaseDate < s2.releaseDate OR (s1.releaseDate = s2.releaseDate AND s1.name < s2.name)))
    
UPDATE sets s
SET s.nextSet = (SELECT next_table.nextSet
	FROM (SELECT temp_next1.currSet, min(temp_next1.nextSet) AS nextSet, temp_next1.nextReleaseDate AS nextReleaseDate
		FROM temp_next AS temp_next1
		WHERE (temp_next1.currSet, temp_next1.nextReleaseDate) in (SELECT temp_next0.currSet, min(temp_next0.nextReleaseDate)
			FROM temp_next AS temp_next0
			GROUP BY temp_next0.currSet) OR temp_next1.nextReleaseDate IS NULL
		GROUP BY temp_next1.currSet) AS next_table
    WHERE s.name = next_table.currSet
);

SELECT s.name, s.prevSet, s.nextSet
FROM sets s