SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT unique_partners) AS unique_partners,
FROM
    DailySales
GROUP BY
    date_id, make_name
;