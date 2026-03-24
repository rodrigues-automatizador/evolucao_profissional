/*
Desafio 1:
Escreva uma instrução SQL que obtém vend_id, vend_name, vend_address e vend_city da tabela Vendors
renomeando vend_name para vname, vend_city para vcity, vend_adress para vaddress, 
classifique por nome do fornecedor
*/

SELECT vend_id, 
	   vend_name AS vname,
	   vend_address AS vaddress,
	   vend_city AS vcity

FROM Vendors
ORDER BY vname;


/*
Desafio 2:
Escreva uma instrução SQL que retorne prod_id, prod_price e sale_price da tabela Products
sale_price é um campo calculado que obtém o preço de venda.
*/

SELECT prod_id,
       prod_price,
	   prod_price * 0.9 AS sale_price
FROM Products
ORDER BY sale_price;