SELECT s.name AS setName, count(*) AS count
FROM sets AS s, (SELECT ptg1.name AS name, min(s1.releaseDate) AS firstReleaseDate
FROM printings ptg1, sets s1
WHERE ptg1.setCode = s1.code
GROUP BY ptg1.name) temp0
JOIN
(SELECT ptg2.name AS name, s2.code AS code, s2.releaseDate AS releaseDate
FROM printings ptg2, sets s2
WHERE ptg2.setCode = s2.code) temp1
ON temp0.name = temp1.name AND temp0.firstReleaseDate = temp1.releaseDate
WHERE s.code = temp1.code
GROUP BY temp1.code
ORDER BY count DESC