WITH temp as (SELECT t.type, ptg.artist, count(*) AS count
	FROM printings ptg JOIN types t ON ptg.name = t.card
	WHERE ptg.rarity="common" OR ptg.rarity="uncommon" 
	GROUP BY t.type, ptg.artist)

SELECT temp_0.*
FROM temp as temp_0 LEFT JOIN temp as temp_1 ON temp_0.type=temp_1.type AND temp_0.count < temp_1.count
WHERE temp_1.count IS NULL
ORDER BY temp_0.count DESC;