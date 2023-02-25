SELECT s.block AS Block, avg(length(c.text)) AS AvgTextLength
FROM cards c, printings ptg, sets s
WHERE c.name = ptg.name AND s.code = ptg.setCode
GROUP BY s.block
HAVING s.block IS NOT NULL
ORDER BY AvgTextLength DESC