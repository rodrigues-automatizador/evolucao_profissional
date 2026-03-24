/*
Desafio 1:
Escreva uma instrução SQL usando INNER JOIN para obter o nome do cliente
(cust_name em Customers) e todos os números de pedidos (order_num em Orders) para cada um.
*/

SELECT Customers.cust_name, 
	   COUNT(Orders.order_num) AS num_ord
FROM Customers
INNER JOIN Orders
ON Customers.cust_id = Orders.cust_id
GROUP BY Customers.cust_id;


/*
Desafio 2:
Modifique a instrução SQL que você acabou de criar para listar
todos os clientes, mesmo aqueles sem pedidos.
*/

SELECT Customers.cust_name,
	   COUNT(Orders.order_num) AS num_ord
FROM Customers
LEFT JOIN Orders
ON Customers.cust_id = Orders.cust_id
GROUP BY Customers.cust_name;


/*
Desafio 3:
Use um OUTER JOIN para juntar tabelas Products e OrderItems
retornando uma lista classificada de nomes de produtos(prod_name)
e os números de pedidos (order_num) associados a cada um.
*/

SELECT prod_name, order_num
FROM Products
LEFT OUTER JOIN OrderItems
ON Products.prod_id = OrderItems.prod_id
ORDER BY prod_name


/*
Desafio 4:
Modifique a instrução criada no desafio anterior para que ela
retorne um número total de pedidos oara cada item (em oposição
aos números dos pedidos).
*/

SELECT Products.prod_name, SUM(order_num) AS total_order
FROM Products
LEFT OUTER JOIN OrderItems
ON Products.prod_id = OrderItems.prod_id
GROUP BY prod_name
ORDER BY prod_name


/*
Desafio 5:
Escreva uma instrução SQL para listar os fornecedores (vend_id em Vendors)
e o número de produtos que eles tem disponíveis, incluindo fornecedores sem produtos
que eles tem disponíveis, incluindo fornecedores sem produtos. Recomenda-se OUTER JOIN
e a função de agregação COUNT() para contar o número de produtos para cada fornecedor
na tabela Products.
*/

SELECT Vendors.vend_id, COUNT(prod_id) AS prod_count
FROM Vendors
LEFT OUTER JOIN Products
ON Vendors.vend_id = Products.vend_id
GROUP BY Vendors.vend_id
ORDER BY Vendors.vend_id