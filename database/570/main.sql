SELECT
    Employee.name AS name
FROM
    Employee
JOIN
    Employee AS Manager
ON
  Employee.id = Manager.id
GROUP BY
    Manager.managerId
HAVING
    COUNT(*) >=5
;