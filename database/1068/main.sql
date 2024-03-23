Select 
    p.product_name AS product_name,
    s.year AS year,
    s.price AS price
FROM
    Product AS p
JOIN
    Sales AS s
WHERE
    p.product_id = s.product_id
;