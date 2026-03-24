/*
Desafio 1:
Escreva uma instrução SQL para obter todos os nomes de clientes
da tabela customers e exiba os resultados classificados de (Z a A)
*/

SELECT cust_name
FROM Customers
ORDER BY cust_name DESC;


/*
Desafio 2:
Escreva uma instrução SQL para obter a ID do cliente e o número do pedido
da tabela Orders e classifique os resultados primeiro pelo ID do cliente
e depois pela data do pedido em ordem cronológica
*/

SELECT cust_id, order_num
FROM ORDERS
ORDER BY cust_id, order_date

/*
Desafio 3:
Nossa loja ficticia obviamente prefere vender itens mais caros e em grande quantidade.
Escreva uma instrução SQL para exibir a quantidade e o preço, classificados primeiro
pela quantidade maiores e pelo preço mais alto.
*/

SELECT quantity, item_price
FROM OrderItems
ORDER BY quantity, item_price DESC;

/*
Desafio 4:
O que há de errado com a seguinte instrução SQL?
*/

SELECT vend_name
FROM Vendors
ORDER BY vend_name DESC;