CREATE TABLE newProducts (
	prod_id CHAR(10) NOT NULL,
	vend_id CHAR(10) NOT NULL,
	prod_name CHAR(254) NOT NULL,
	prod_price NUMERIC(8, 2) NOT NULL,
	prod_desc VARCHAR(1000) NULL
);


CREATE TABLE newOrders (
	order_num INTEGER NOT NULL,
	order_date DATE NOT NULL,
	cust_id CHAR(10) NOT NULL
)


CREATE TABLE newOrderItems (
	order_num INTEGER NOT NULL,
	order_item INTEGER NOT NULL,
	prod_id CHAR(10) NOT NULL,
	quantity INTEGER NOT NULL DEFAULT 1,
	item_price NUMERIC(8, 2) NOT NULL
)


ALTER TABLE Vendors
ADD vend_phone CHAR(20);


ALTER TABLE Vendors
DROP COLUMN vend_phone;


DROP TABLE newOrders
DROP TABLE newOrderItems
DROP TABLE newProducts
DROP TABLE custcopy