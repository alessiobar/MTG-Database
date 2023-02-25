SELECT s.name AS name, s.totalSetSize AS setSize, round(sum(p.normal),2) AS totalNormalPrice, round(sum(p.foil),2) AS totalFoilPrice, round((sum(p.foil)/sum(p.normal)),2) AS FoilMarkup
FROM sets s, printings ptg, prices p
WHERE s.code = ptg.setCode AND ptg.uuid = p.uuid AND s.isFoilOnly = "0"
GROUP BY ptg.setCode
HAVING FoilMarkup IS NOT NULL
ORDER BY FoilMarkup DESC