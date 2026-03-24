SELECT prod_name
FROM Products;

SELECT prod_id, prod_name, prod_price
FROM Products;

SELECT *
FROM Products;

SELECT vend_id -- isto é um comentário
FROM Products;

/* Isto é um comentário */
SELECT DISTINCT vend_id
FROM Products;

SELECT prod_name
FROM Products
LIMIT 5;

SELECT prod_name
FROM Products
LIMIT 5 OFFSET 5;