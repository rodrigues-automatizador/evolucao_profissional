/* Inserção de dados na tabela com base no retorno da query */ 
INSERT INTO Cliente (nome)
					SELECT cust_name
					FROM Customers;

/* Criação de uma tabela temporária e dados copiados do retorno da query */ 
CREATE TABLE CustCopy AS SELECT * FROM Customers;