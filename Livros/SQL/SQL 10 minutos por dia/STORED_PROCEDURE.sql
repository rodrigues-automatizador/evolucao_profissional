CREATE PROCEDURE procMailingListCount(OUT ListCount INTEGER)
LANGUAGE plpgsql
AS $$
DECLARE
    v_rows INTEGER;
BEGIN
    SELECT COUNT(*) INTO v_rows
    FROM Customers
    WHERE cust_email IS NOT NULL;

    ListCount := v_rows;
END;
$$;


CREATE OR REPLACE PROCEDURE procNewOrder(OUT var_order_num INTEGER, IN p_cust_id CHAR(10))
LANGUAGE plpgsql
AS $$
BEGIN
    -- Pega o maior número de pedido atual (ou 0 se não houver pedidos)
    SELECT COALESCE(MAX(order_num), 0)
    INTO var_order_num
    FROM Orders;

    -- Incrementa para o novo pedido
    var_order_num := var_order_num + 1;

    -- Insere o novo pedido
    INSERT INTO Orders(order_num, order_date, cust_id)
    VALUES (var_order_num, CURRENT_DATE, p_cust_id);
END;
$$;