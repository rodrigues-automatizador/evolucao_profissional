/*
Desafio 1:
Escreva uma instrução SQL que retorne ID do cliente o nome do cliente e o user_login

*/
SELECT cust_id, cust_name, cust_city,
UPPER(LEFT(cust_contact, 2)) ||
UPPER(LEFT(cust_city, 3)) AS user_login
FROM Customers


/*
Desafio 2:
Escreva uma instrução SQL para retornar o número do pedido order_num e data do pedido para todos
os pedidos em janeiro de 2020 classificados por data do pedido.
*/

SELECT order_num, order_date
FROM Orders
WHERE order_date BETWEEN to_date('2020-01-01', 'yyyy-mm-dd')
AND to_date('2020-01-31', 'yyyy-mm-dd');