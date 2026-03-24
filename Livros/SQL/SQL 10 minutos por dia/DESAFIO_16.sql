/* 
Desafio 1:
Adicione uma coluna de site (vend_web) à tabela Vendors. Você precisa
de um campo de texto grande o suficiente para acomodar uma URL.
*/

ALTER TABLE Vendors
ADD vend_web VARCHAR(100);


/*
Desafio 2:
Use as intruções UPDATE para atualizar os registros de Vendor para
incluir um site.
*/

UPDATE Vendors
SET vend_web = 'https://www.google.com.br/'