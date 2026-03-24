CREATE INDEX idx_nome_cliente
ON clientes(nome);

CREATE INDEX idx_tags_gin
ON artigos USING gin(tags)

CREATE INDEX idx_cliente_nome_email
ON clientes(nome,email)

CREATE INDEX idx_email_unico
ON clientes(email);

CREATE INDEX idx_ativos
ON clientes(nome)
WHERE ativo = TRUE


CREATE INDEX idx_lower_nome
ON clientes(LOWER(nome))


REINDEX INDEX idx_nome_cliente


EXPLAIN ANALYSE SELECT * FROM clientes WHERE nome = 'Ana Maria'

------------------------

SELECT * FROM clientes
WHERE nome = 'Ana Maria'

SELECT * FROM clientes
ORDER BY nome;

SELECT * FROM clientes
WHERE email = 'ana.maria@example.com'

SELECT clientes.nome, pedidos.valor_total
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.client_id


SELECT clientes.nome, pedidos.valor_total
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.client_id;

SELECT pedidos.id, clientes.nome
FROM pedidos
RIGHT JOIN clientes ON pedidos.client_id = clientes.id;

SELECT clientes.nome, pedidos.valor_total
FROM clientes
FULL JOIN pedidos ON clientes.id = pedidos.client_id;

SELECT clientes.nome, produtos.nome
FROM clientes
CROSS JOIN produtos

select * from produtos


SELECT nome
FROM clientes
WHERE id IN (
	SELECT client_id
	FROM pedidos
	WHERE valor_total > 500
)


SELECT media_valor
FROM (
	SELECT AVG(valor_total) AS media_valor
	FROM pedidos
)

WITH pedidos_valiosos AS (SELECT client_id, valor_total 
						  FROM pedidos
						  WHERE valor_total > 500)
SELECT clientes.nome, pedidos_valiosos.valor_total
FROM clientes
JOIN pedidos_valiosos ON
clientes.id = pedidos_valiosos.client_id


WITH clientes_ativos AS ( SELECT id, nome 
						  FROM clientes 
						  WHERE ativo = TRUE), 
	 
	 pedidos_ultimos_30_dias AS ( SELECT client_id, COUNT(*) AS total
	 							  FROM pedidos
								  WHERE data_pedido >= CURRENT_DATE - INTERVAL '30 days'
								  GROUP BY client_id
								  )
SELECT c.nome, p.total
FROM clientes_ativos c
LEFT JOIN pedidos_ultimos_30_dias p
ON c.id = p.client_id


ALTER TABLE funcionarios
ALTER COLUMN chefe TYPE INTEGER USING chefe::INTEGER;



WITH RECURSIVE hierarquia AS ( SELECT id, nome, id_chefe
							   FROM funcionarios
							   WHERE id_chefe IS NULL UNION ALL
							   SELECT f.id, f.nome, f.chefe
							   
							   FROM funcionarios f
							   INNER JOIN hierarquia h ON f.id_chefe = h.id
							   )

SELECT * FROM hierarquia;			


SELECT p.nome AS produto,
	   c.nome AS cliente
FROM vendas v
INNER JOIN produtos p ON
v.produto_id = p.id
INNER JOIN clientes c ON
v.cliente_id = c.id


ALTER TABLE vendas ADD COLUMN produto_id INTEGER

CREATE TABLE vendas (
	id SERIAL PRIMARY KEY,
	cliente_id INTEGER
)

SELECT c.nome
FROM clientes c
LEFT JOIN pedidos p ON
c.id = p.client_id


WITH vendas_recentes AS (
	SELECT client_id, SUM(valor_total) AS total
	FROM pedidos
	WHERE data_pedido >= CURRENT_DATE - INTERVAL '90 days'
	GROUP BY client_id
)

SELECT c.nome, v.total
FROM clientes c
JOIN vendas_recentes v ON
c.id = v.client_id;

SELECT COUNT(*) AS total_
FROM clientes

SELECT SUM(valor_total) AS receita_total
FROM pedidos


SELECT client_id, SUM(valor_total) AS total_pedidos
FROM pedidos
GROUP BY client_id


ALTER TABLE clientes ADD COLUMN telefone VARCHAR(10)

ALTER TABLE clientes DROP COLUMN telefone

SELECT LOWER(nome) FROM clientes

SELECT ROUND(valor_total, 2) FROM pedidos

SELECT COALESCE(telefone, 'Não informado') FROM clientes

SELECT nome, ROW_NUMBER() OVER (ORDER BY nome) AS posicao
FROM clientes

SELECT client_id, valor_total, SUM(valor_total) 
OVER (PARTITION BY client_id ORDER BY data_pedido) AS acumulado
FROM pedidos


SELECT c.nome, COUNT(p.id) AS total_pedidos
FROM clientes c
LEFT JOIN pedidos p ON 
c.id = p.client_id
GROUP BY c.nome
ORDER BY total_pedidos DESC

WITH pedidos_numerados AS (
	SELECT id, client_id, data_pedido,
	ROW_NUMBER() OVER(PARTITION BY client_id 
	ORDER BY data_pedido) AS rn
	FROM pedidos
)
SELECT id, client_id, data_pedido
FROM pedidos_numerados
WHERE rn = 1

SELECT client_id, MAX(valor_total) AS maior_pedido
FROM pedidos
GROUP BY client_id

SELECT DATE_TRUNC('month', data_pedido) AS mes,
SUM(valor_total) AS total_mensal
FROM pedidos
GROUP BY mes
ORDER BY mes;


CREATE TABLE contas (
id SERIAL PRIMARY KEY,
saldo NUMERIC(10,2)
)

INSERT INTO CONTAS (ID, SALDO) VALUES (2, 60)

BEGIN;
UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;

BEGIN;
UPDATE contas SET saldo = saldo - 5000 WHERE id = 1;

ROLLBACK;

SELECT * FROM CLIENTES

BEGIN;
INSERT INTO clientes(nome) VALUES ('Carlos Teste');
SAVEPOINT primeiro_passo;
INSERT INTO clientes(nome) VALUES ('Erro simulado');
ROLLBACK TO SAVEPOINT primeiro_passo;
COMMIT;

CREATE ROLE analista;

CREATE ROLE maria LOGIN PASSWORD 'ABC@123teste'

CREATE ROLE gestor LOGIN CREATEDB PASSWORD 'ABC@123teste'

GRANT analista TO maria;

GRANT SELECT ON clientes TO analista;
GRANT INSERT ON clientes TO analista;

GRANT SELECT, UPDATE, DELETE ON clientes TO gestor;

CREATE SCHEMA vendas;

GRANT CREATE ON SCHEMA vendas TO maria;

GRANT SELECT ON clientes TO analista WITH GRANT OPTION;

REVOKE INSERT ON clientes FROM analista;

REVOKE ALL ON clientes FROM gestor

REVOKE analista FROM maria;

CREATE SCHEMA aplicacao

CREATE ROLE desenvolvedores;
GRANT SELECT, INSERT, UPDATE
ON ALL TABLES IN SCHEMA aplicacao 
TO desenvolvedores;

CREATE OR REPLACE VIEW vw_clientes_ativos AS
SELECT id, nome, email
FROM clientes
WHERE ativo = TRUE

DROP VIEW vw_clientes_ativos

DROP VIEW IF EXISTS vw_clientes_ativos;

SELECT * FROM vw_clientes_ativos


SELECT p.id, p.valor_total, c.nome
FROM pedidos p
JOIN vw_clientes_ativos c ON
p.client_id = c.id;


SELECT * FROM vw_clientes_ativos


CREATE MATERIALIZED VIEW mvw_resumo_vendas AS
SELECT client_id, SUM(valor_total) AS total_compras
FROM pedidos
GROUP BY client_id;

SELECT * FROM mvw_resumo_vendas

REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_resumo_vendas

CREATE OR REPLACE FUNCTION func_saudacao_usuario(
nome TEXT)

RETURNS TEXT AS $$
BEGIN
RETURN 'Bem vindo, ' ||nome||'!';
END;
$$ LANGUAGE plpgsql;

SELECT func_saudacao_usuario('Carlos')


CREATE OR REPLACE FUNCTION func_calcular_desconto(valor NUMERIC)

RETURNS NUMERIC AS $$

DECLARE
desconto NUMERIC;

BEGIN
	IF valor > 1000 THEN
		desconto := valor * 0.10;
		
	ELSE
		desconto := valor * 0.05;
		
	END IF;

	RETURN desconto;

END;
$$ LANGUAGE plpgsql;

SELECT func_calcular_desconto(800)


DROP PROCEDURE proc_ajustar_estoque

CREATE OR REPLACE PROCEDURE proc_ajustar_estoque(
	p_produto_id INT, 
	p_quantidade INT
)

LANGUAGE plpgsql AS $$

BEGIN
	UPDATE estoque
	SET quantidade = quantidade + p_quantidade
	WHERE produto_id = p_produto_id;
END;
$$;

CALL proc_ajustar_estoque(1, -20);

SELECT * FROM estoque
SELECT * FROM produtos

INSERT INTO produtos (nome, descricao)
VALUES ('Camiseta Basicamente', 'Camiseta com algodão Peruano e anti odor')

INSERT INTO estoque (produto_id, local_id, quantidade)
VALUES (1, 1, 10)


CREATE TABLE logs (
	mensagem VARCHAR(50)
)

SELECT * FROM logs

DO $$
BEGIN
	INSERT INTO logs(mensagem) 
	VALUES('Execução rápida via bloco anônimo');
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION func_listar_numeros()

RETURNS VOID AS $$

DECLARE
	i INTEGER := 1;

BEGIN
	WHILE i <= 5 LOOP
		RAISE NOTICE 'Número: %', i;
		i := i + 1;
	END LOOP;
END;

$$LANGUAGE plpgsql;

SELECT func_listar_numeros()