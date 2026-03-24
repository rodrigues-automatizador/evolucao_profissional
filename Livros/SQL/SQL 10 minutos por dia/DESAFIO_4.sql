/* 
Desafio: 01
Escreva uma instrução SQL para obter o nome do fornecedor da tabela vendors
retornando apenas fornecedores na California, requer por país e estado.
*/

SELECT vend_name
FROM Vendors
WHERE vend_country = 'USA'
AND vend_state = 'CA'
ORDER BY vend_name


/*
Desafio 2:
Escreva uma instrução SQL para encontrar todos os pedidos que incluem pelo menos 100 dos itens
BR01, BR02, BR03. Você deve retornar o número do pedido order_num id do produto
e a quantidade da tabela OrderItems filtrando pela ID e pela quantidade do produto
*/

SELECT order_num, prod_id
FROM OrderItems
WHERE prod_id IN ('BR01','BR02','BR03')
AND quantity >= 100
ORDER BY prod_id;


/* 
Desafio 3:
Escreva uma instrução SQL que retorne o nome prod_name e o preço do produto
da tabela Products para todos os produtos com preços entre 3 e 6.
*/


SELECT prod_name, prod_price
FROM Products
WHERE prod_price BETWEEN 3 AND 6
ORDER BY prod_price;


/*
Desafio 4:
O que há de errado com a seguinte instrução SQL:

SELECT vend_name
FROM Vendors
ORDER BY vend_name
WHERE vend_country = 'USA'
AND vend_state = 'CA'
*/

SELECT vend_name
FROM Vendors
WHERE vend_country = 'USA'
AND vend_state = 'CA'
ORDER BY vend_name