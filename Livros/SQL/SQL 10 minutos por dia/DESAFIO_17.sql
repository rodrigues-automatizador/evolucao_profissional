/*
Desafio 1:
*/

CREATE VIEW vwCustomersWithOrders AS
SELECT Customers.* 
FROM Customers
INNER JOIN Orders ON
Customers.cust_id = Orders.cust_id;


SELECT * FROM vwCustomersWithOrders

/*
Desafio 2:
O que há de errado com a seguinte instrução SQL?
*/

CREATE VIEW vwOrderItemsExpanded AS
SELECT order_num,
	   prod_id,
	   quantity,
	   item_price,
	   quantity * item_price AS expanded_price
FROM OrderItems
ORDER BY order_num;