SELECT
    a.id AS id
FROM
    weather AS a
CROSS JOIN
    weather AS b
ON
    datediff(a.date, b.date) = 1
WHERE
    a.temp > b.temp
;