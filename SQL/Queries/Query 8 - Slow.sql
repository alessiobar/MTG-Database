SELECT p.uuid, p.normal
FROM prices p JOIN printings ptg ON p.uuid=ptg.uuid JOIN sets s ON ptg.setCode = s.code JOIN cards c ON ptg.name = c.name LEFT JOIN colors col ON c.name = col.card
WHERE p.normal <= 10 AND s.releaseDate >= "2000-01-01" AND c.manaCost RLIKE "[WUBRG]" AND col.card IS NULL
ORDER BY p.normal