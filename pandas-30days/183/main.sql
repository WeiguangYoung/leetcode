SELECT
  name
AS 
  "Customers"
FROM
  customers
WHERE
  customers.id not in (select customerid from orders);

SELECT  name AS "Customers"
FROM customers
LEFT JOIN customers.id == orders.customerid
WHERE customers.customerid is NULL;