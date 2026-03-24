/*
Desafio 1:
Usando INSERT e as colunas especificadas, adicione-se á tabela Customers.
Liste explicitamente as colunas que você está adicionando e apenas as que você precisa.
*/

INSERT INTO Customers (cust_name,
					   cust_contact,
					   cust_contact,
					   cust_email,
					   cust_state,
					   cust_city)
			   VALUES ('Éder Rodrigues de Souza',
			   		   '11980535694',
					   'ederrsouza@gmail.com',
					   'SP',
					   'Sao Paulo')

/*
Desafio 2:
Faça cópias de backup de suas tabelas Orders e OrderItems 
*/					   

CREATE TABLE newOrders AS SELECT * FROM Orders;					  

CREATE TABLE newOrderItems AS SELECT * FROM OrderItems;