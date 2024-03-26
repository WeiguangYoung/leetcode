SELECT product_id, IFNULL(ROUND(SUM(sales) / SUM(units), 2), 0) AS average_price
FROM (
        SELECT p.product_id, u.units, p.price * u.units AS sales
        FROM prices AS p
            LEFT JOIN UnitsSold AS u ON p.product_id = u.product_id
            AND (
                u.purchase_date BETWEEN p.start_date AND p.end_date
            )
    ) AS T
GROUP BY
    product_id;