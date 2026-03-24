/*
Desafio 1:
Escreva uma instrução SQL para obter ID do produto e o nome do produto
da tabela Products, retornando apenas com um preço de 9.49.
*/

SELECT prod_id, prod_name
FROM Products
WHERE prod_price = 9.49;


/* 
Desafio 2:
Escreva uma instrução SQL para obter ID do produto e o nome do produto
da tabela Products retornando apenas produtos com um preço de 9 ou mais.
*/

SELECT prod_id, prod_name
FROM Products
WHERE prod_price >= 9;


/* 
Desafio 3:
Escreva uma instrução SQL para obter a lista exclusiva de numeros de pedidos
da tabela OrderItems que comtém 100 ou mais items.
*/


SELECT order_num, quantity
FROM OrderItems
WHERE quantity >= 100;

/* 
Desafio 4:
Escreva uma instrução SQL que retorne o nome do produto e o preço da tabela Products
para todos os produtos com preços entre 3 e 6 e classifique os resultados por preço.
*/

SELECT prod_name, prod_price
FROM Products
WHERE prod_price BETWEEN 3 AND 6
ORDER BY prod_price;