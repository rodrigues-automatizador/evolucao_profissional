/*
Desafio 1:
Escreva uma instrução SQL para retornar o nome do cliente(cust_name) da tabela Customers
e números de pedidos relacionados(order_num) da tabela Orders, classificando o resultado
por nome do cliente e, em seguida, pelo número do pedido. Na verdade, tente este desafio duas vezes
uma vez usando a sintaxe simples de equijoin e uma vez usando INNER JOIN.
*/

SELECT cust_name, order_num
FROM Customers, Orders
WHERE Customers.cust_id = Orders.cust_id
ORDER BY cust_name;

SELECT cust_name, order_num
FROM Customers 
INNER JOIN Orders
ON Customers.cust_id = Orders.cust_id
ORDER BY cust_name;


/*
Desafio 2:
Vamos tornar o desafio anterior mais útil. Além de retornar o nome do cliente 
e o número do pedido, adicione uma terceira coluna chamada OrderTotal, contendo
o preço total de cada pedido. Há duas maneiras de fazer isso: você pode criar a 
coluna OrderTotal usando uma subconsulta na tabela OrderItems ou pode juntar
a tabela OrderItems as tabelas existentes e usar uma função de agregação.
*/

SELECT cust_name, order_num, (SELECT SUM(quantity * item_price)
							  FROM OrderItems
							  WHERE Orders.order_num = OrderItems.order_num)
							  AS Order_total
FROM Customers
INNER JOIN Orders
ON Customers.cust_id = Orders.cust_id
ORDER BY cust_name;


/*
Desafio 3:
Escreva uma instrução que obtenha as datas quando o produto BR01 foi pedido,
mas desta vez use uma junção e a sintaxe de equijoin simples. O resultado deve
ser identico ao da Lição 2.
*/

SELECT cust_id, order_date
FROM Orders, OrderItems
WHERE Orders.order_num = OrderItems.order_num
AND OrderItems.prod_id = 'BR01'
ORDER BY order_date;


/*
Desafio 4:
Recrie o SQL que você escreveu no desafio 3, mas desta vez usando a sintaxe INNER JOIN.
O código que você escreveu lá usou duas subconsultas aninhadas. Para recriá-lo,
você precisará de duas instruções INNER JOIN, cada uma formatada como exemplo INNER JOIN
mostrado anteriormente nesta lição. E não se esqueça da cláusula WHERE para filtrar por prod_id.
*/

SELECT cust_id, order_date
FROM Orders
INNER JOIN OrderItems
ON Orders.order_num = OrderItems.order_num
WHERE OrderItems.prod_id = 'BR01'
ORDER BY order_date;


/*
Desafio 5:
Escreva uma instrução SQL que use junções para retornar o nome do cliente (cust_name)
da tabela Customers e o preço total de todos os pedidos da tabela OrderItems. Aqui está
uma dica: para juntar essas tabelas, você também precisará incluir a tabela Orders (porque Customers
não está relacionada a Orders e Orders está relacionada a OrderItems). Não se esqueça de GROUP BY
e HAVING, e classifique os resultados por nome do cliente. Você pode usar equijoin simples
ou INNER JOIN para este desafio. Ou, se estiver sentindo corajoso, tente escrever os dois.
*/

