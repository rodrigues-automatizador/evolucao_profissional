CREATE VIEW vwProductCustomers AS 
	SELECT cust_name, cust_contact, prod_id
	FROM Customers, Orders, OrderItems
	WHERE Customers.cust_id = Orders.cust_id
	AND OrderItems.order_num = Orders.order_num;


SELECT cust_name, cust_contact
FROM vwProductCustomers
WHERE prod_id = 'RGAN01'


CREATE VIEW vwVendorLocation AS
SELECT RTRIM(vend_name) || ' (' || RTRIM(vend_country) || ')' AS vend_title
FROM Vendors;


CREATE VIEW vwCustomersEmailList AS
SELECT cust_id, cust_name, cust_email
FROM Customers
WHERE cust_email IS NOT NULL;


CREATE VIEW vwOrderItemsExpanded AS
SELECT order_num,
	   prod_id,
	   quantity,
	   item_price,
	   quantity * item_price AS expanded_price
FROM OrderItems;	


SELECT * FROM vwOrderItemsExpanded
WHERE order_num = 20008

