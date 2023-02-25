SELECT supc.card AS card, supc.keyword AS keyword, r.ruling AS ruling
FROM rulings r, (SELECT *
	FROM keywords k
    WHERE EXISTS (SELECT *
		FROM supertypes AS supt
        WHERE k.card = supt.card)) supc
WHERE r.card = supc.card AND r.ruling LIKE CONCAT("%",supc.keyword,"%")