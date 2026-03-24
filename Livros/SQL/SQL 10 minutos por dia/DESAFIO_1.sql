/* 
Desafio 1:
Escreva uma instrução SQL para obter todas as ID's
de (cust_id) da tabela Customers
*/

SELECT cust_id
FROM Customers;

/*
Desafio 2:
Escreva uma instrução SQL para obter uma lista dos produtos pedidos
apenas uma lista de produtos distintos
*/

SELECT DISTINCT prod_id
FROM OrderItems;

/*
Desafio 3:
Escreva uma instrução SQL que obtenha todas as colunas da tabela Customers
e uma instrução alternativa que obtenha apenas a id do cliente
*/


/* Comentando o primeiro SELECT
SELECT *
FROM Customers
*/

SELECT cust_id
FROM Customers;