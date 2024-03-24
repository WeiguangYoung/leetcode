SELECT
    t1.machine_id,
    ROUND(AVG(t2.processing_time), 3) AS processing_time
FROM    
    (
    SELECT
        machine_id,
        process_id,
        (max(timestamp)-min(timestamp)) AS processing_time
    FROM
        activity
    GROUP BY
        machine_id, process_id
    ) AS t1
GROUP BY
    t1.machine_id
;