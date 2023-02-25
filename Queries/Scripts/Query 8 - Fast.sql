SELECT p.uuid, p.normal
FROM prices p
WHERE p.normal <= 10 AND p.uuid IN (
	SELECT ptg.uuid
	FROM printings ptg
    WHERE ptg.setCode IN (
		SELECT s.code
        FROM sets s
        WHERE s.releaseDate >= "2000-01-01") AND ptg.name IN (
			SELECT c.name
            FROM cards c
            WHERE c.manaCost RLIKE "[WUBRG]" AND c.name NOT IN(
				SELECT col.card
				FROM colors col)))
ORDER BY p.normal