SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE 'Fish%'


SELECT cust_contact
FROM Customers 
WHERE cust_contact SIMILAR TO '(J|M)%'
ORDER BY cust_contact;


SELECT cust_contact
FROM Customers
WHERE cust_contact SIMILAR TO '(^J|M)%'
ORDER BY cust_contact;


