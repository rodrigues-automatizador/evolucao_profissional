/*
Desafio 1:
Escreva uma instrução SQL que combine duas instruções SELECT
que obtem a Id do produto (prod_id) e quantity da tabela OrderItems,
uma filtrando por linhas com ma quantidade de exatamente 100 e a outra
filtrando por produtos com uma ID que começa com uma ID BNBG.
Classifique os resultados por ID do produto.
*/

SELECT prod_id, quantity
FROM OrderItems
WHERE quantity = 100
UNION ALL
SELECT prod_id, quantity
FROM OrderItems
WHERE prod_id LIKE 'BNBG%'
ORDER BY prod_id


/*
Desafio  2:
Reescreva a instrução SQL que você acabou de criar para usar
uma única instrução SELECT.
*/

SELECT prod_id, quantity
FROM OrderItems
WHERE quantity = 100
OR prod_id LIKE 'BNBG%'
ORDER BY prod_id


/*
Desafio 3:
Escreva uma instrução SQL que retorne e combine o nome do produto (prod_name)
de Products e o nome do cliente (cust_name) de Customers e classifique o resultado
pelo nome do Produto
*/


SELECT prod_name
FROM Products
UNION
SELECT cust_name
FROM Customers
ORDER BY prod_name

/*
Desafio 4:
O que há de errado com a seguinte instrução SQL.
*/

SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_state = 'MI'
UNION
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_state = 'IL'
ORDER BY cust_name;