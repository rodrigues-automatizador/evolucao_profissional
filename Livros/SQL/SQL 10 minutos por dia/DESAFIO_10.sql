/*
Desafio 1:
Usando uma subconsulta, retorne uma lista de clientes que compraram itens
com preço de 10 ou mais. Recomenda-se usar a tabela OrderItems para encontrar
os números de pedidos correspondentes (order_num) e, em seguida, a tabela Orders
para obter a ID do cliente cust_id para esses pedidos.
*/

SELECT cust_id
FROM Orders
WHERE order_num IN (SELECT order_num 
				    FROM OrderItems
					WHERE item_price > 10)

/*
Desafio 2:
Você precisa saber as datas em que o produto BR01 foi encomendado.
Escreva uma instrução SQL que usa uma subconsulta para determinar quais
pedidos (em OrderItems) continham itens com prod_id igual a BR01 e então
retorne a ID do cliente (cust_id) e a data do pedido (order_date) para cada pedido
da tabela Orders. Classifique os resultados pela data do pedido.
*/

SELECT cust_id, order_date
FROM Orders
WHERE order_num IN (SELECT order_num
					FROM OrderItems
					WHERE prod_id = 'BR01')
ORDER BY order_date;


/*
Desafio 3:
Agora vamos tornar as coisas um pouco mais desafiadoras. Atualize o desafio anterior
para retornar o email do cliente (cust_email) na tabela Customers para todos os clientes
que compraram itens com prod_id igual a BR01. 
*/

SELECT cust_email
FROM Customers
WHERE Customers.cust_id IN (SELECT cust_id
							FROM Orders
							WHERE order_num IN (SELECT order_num
												FROM OrderItems
												WHERE prod_id = 'BR01'))


/*
Desafio 4:
Precisamos de uma lista de IDs de clientes com o valor total de seus pedidos.
Escreva uma instrução SQL para retornar a ID do cliente (cust_id da tabela Orders)
e total_ordered usando uma subconsulta para retornar o total de pedidos para cada cliente.
Classifique os resultados por valor gasto de maior para o menor.
*/

SELECT cust_id, 
	   (SELECT SUM(item_price * quantity)
	    FROM OrderItems
		WHERE Orders.order_num = OrderItems.order_num) AS total_ordered
FROM Orders
ORDER BY total_ordered DESC;


/*
Desafio 5:
Escreva uma instrução SQL que obtenha todos os nomes de produtos
da tabela Products, junto com uma coluna calculada chamada quant_sold
contendo o numero total vendido deste item.
*/

SELECT prod_name,
				(SELECT SUM(quantity)
				 FROM OrderItems
				 WHERE Products.prod_id = OrderItems.prod_id) AS quant_sold
FROM Products;