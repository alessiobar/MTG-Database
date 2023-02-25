SELECT cols.color AS color, count(*) AS count
FROM cards c JOIN colors cols ON c.name = cols.card JOIN legalities l ON c.name = l.card JOIN types t on c.name = t.card
WHERE ((CAST(c.power AS SIGNED) > 9) AND (CAST(c.toughness AS SIGNED) > 9)) AND t.type = "Creature" AND l.legacy = "Legal"
GROUP BY cols.color