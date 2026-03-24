/*
Desafio 1:
Escreva uma instrução SQL para obter o nome do produto e a descrição
da tabela produtos, retornando apenas os produtos em que a palavra
toy estena na descrição
*/

SELECT prod_name, prod_desc
FROM Products
WHERE prod_desc LIKE '%toy%'
ORDER BY prod_name;


/*
Desafio 2:
Inverter o desafio e não apresentar a palavra toy na descrição.
*/


SELECT prod_name, prod_desc
FROM Products
WHERE prod_desc NOT LIKE '%toy%'
ORDER BY prod_name;


SELECT prod_name, prod_desc
FROM Products
WHERE prod_desc NOT SIMILAR TO '%toy%'
ORDER BY prod_name;


/* 
Desafio 3:
Escreva uma instrução SQL para obter o nome do produto e a descrição,
retornando apenas produtos em que a palavra toye carrots apareçam na descrição.
*/

SELECT prod_name, prod_desc
FROM Products
WHERE prod_desc LIKE '%toy%'
AND prod_desc LIKE '%carrots%'
ORDER BY prod_desc;


/*
Desafio 4:
Escreva uma instrução SQL para obter o nome do produto e a descrição
a palavra toy precisa aparecer antes da palavra carrots
*/

SELECT prod_name, prod_desc
FROM Products
WHERE prod_desc LIKE '%toy%carrots%'
ORDER BY prod_name;