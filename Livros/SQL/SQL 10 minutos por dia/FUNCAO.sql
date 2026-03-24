SELECT vend_name, UPPER(vend_name) AS vend_name_upcase
FROM Vendors
ORDER BY vend_name


SELECT order_num
FROM Orders
WHERE DATE_PART('year', order_date) = 2020;


SELECT Order_num
FROM Orders
WHERE order_date BETWEEN to_date('2020-01-01','yyyy-mm-dd')
AND to_date('2020-12-31','yyyy-mm-dd')