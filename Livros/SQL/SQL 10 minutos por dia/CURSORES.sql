CREATE INDEX idx_prod_name
ON Products (prod_name);


CREATE OR REPLACE FUNCTION fn_customers_state()
RETURNS trigger AS $$
BEGIN
  NEW.cust_state := UPPER(NEW.cust_state);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER trg_customers_state
BEFORE INSERT OR UPDATE
ON customers
FOR EACH ROW
EXECUTE FUNCTION fn_customers_state();