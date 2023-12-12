ALTER TABLE orders_table ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;
ALTER TABLE orders_table ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID;
ALTER TABLE orders_table ALTER COLUMN card_number TYPE VARCHAR(19) USING card_number::VARCHAR(19);
ALTER TABLE orders_table ALTER COLUMN store_code TYPE VARCHAR(11) USING store_code::VARCHAR(11);
ALTER TABLE orders_table ALTER COLUMN product_code TYPE VARCHAR(11) USING product_code::VARCHAR(11);
ALTER TABLE orders_table ALTER COLUMN product_quantity TYPE SMALLINT USING product_quantity::SMALLINT;

ALTER TABLE dim_users ALTER COLUMN first_name TYPE VARCHAR(255) USING first_name::VARCHAR(255);
ALTER TABLE dim_users ALTER COLUMN last_name TYPE VARCHAR(255) USING last_name::VARCHAR(255);
ALTER TABLE dim_users ALTER COLUMN date_of_birth TYPE DATE USING date_of_birth::DATE;
ALTER TABLE dim_users ALTER COLUMN country_code TYPE VARCHAR(2) USING country_code::VARCHAR(2);
ALTER TABLE dim_users ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID;
ALTER TABLE dim_users ALTER COLUMN join_date TYPE DATE USING join_date::DATE;

UPDATE dim_store_details SET latitude = COALESCE(latitude, lat);
ALTER TABLE dim_store_details DROP COLUMN lat;
ALTER TABLE dim_store_details ALTER COLUMN longitude TYPE FLOAT USING longitude::FLOAT;
ALTER TABLE dim_store_details ALTER COLUMN locality TYPE VARCHAR(255) USING locality::VARCHAR(255);
ALTER TABLE dim_store_details ALTER COLUMN store_code TYPE VARCHAR(11) USING store_code::VARCHAR(11);
ALTER TABLE dim_store_details ALTER COLUMN staff_numbers TYPE SMALLINT USING staff_numbers::SMALLINT;
ALTER TABLE dim_store_details ALTER COLUMN opening_date TYPE DATE USING opening_date::DATE;
ALTER TABLE dim_store_details ALTER COLUMN store_type TYPE VARCHAR(255) USING store_type::VARCHAR(255);
UPDATE dim_store_details SET latitude = NULL WHERE latitude = 'N/A';
ALTER TABLE dim_store_details ALTER COLUMN latitude TYPE FLOAT USING latitude::FLOAT;
ALTER TABLE dim_store_details ALTER COLUMN country_code TYPE VARCHAR(2) USING country_code::VARCHAR(2);
ALTER TABLE dim_store_details ALTER COLUMN continent TYPE VARCHAR(255) USING continent::VARCHAR(255);

UPDATE dim_products SET product_price = REPLACE(product_price, '£', '');
ALTER TABLE dim_products ADD weight_class VARCHAR(20);
UPDATE dim_products 
SET weight_class = CASE
    WHEN weight < 2 THEN 'Light'
    WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
    WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
    ELSE 'Truck_Required'
END;

ALTER TABLE dim_products ALTER COLUMN product_price TYPE FLOAT USING product_price::FLOAT;
ALTER TABLE dim_products ALTER COLUMN weight TYPE FLOAT USING weight::FLOAT;
ALTER TABLE dim_products ALTER COLUMN "EAN" TYPE VARCHAR(255) USING "EAN"::VARCHAR(255);
ALTER TABLE dim_products ALTER COLUMN product_code TYPE VARCHAR(11) USING product_code::VARCHAR(11);
ALTER TABLE dim_products ALTER COLUMN date_added TYPE DATE USING date_added::DATE;
ALTER TABLE dim_products ALTER COLUMN uuid TYPE UUID USING uuid::UUID
ALTER TABLE dim_products RENAME COLUMN removed TO still_available
ALTER TABLE dim_products ALTER COLUMN still_available TYPE BOOLEAN USING (still_available = 'Still_avaliable')
ALTER TABLE dim_products ALTER COLUMN weight_class TYPE VARCHAR(20) USING weight_class::VARCHAR(20)

ALTER TABLE dim_date_times ALTER COLUMN month TYPE VARCHAR(2) USING month::VARCHAR(2);
ALTER TABLE dim_date_times ALTER COLUMN year TYPE VARCHAR(4) USING year::VARCHAR(4);
ALTER TABLE dim_date_times ALTER COLUMN day TYPE VARCHAR(2) USING day::VARCHAR(2);
ALTER TABLE dim_date_times ALTER COLUMN time_period TYPE VARCHAR(7) USING time_period::VARCHAR(7);
ALTER TABLE dim_date_times ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;

ALTER TABLE dim_card_details ALTER COLUMN card_number TYPE VARCHAR(22) USING card_number::VARCHAR(22);
ALTER TABLE dim_card_details ALTER COLUMN expiry_date TYPE VARCHAR(10) USING expiry_date::VARCHAR(10);
ALTER TABLE dim_card_details ALTER COLUMN date_payment_confirmed TYPE DATE USING date_payment_confirmed::DATE;

ALTER TABLE dim_card_details ADD CONSTRAINT dim_card_details_pk PRIMARY KEY (card_number);
ALTER TABLE dim_date_times ADD CONSTRAINT dim_date_times_pk PRIMARY KEY (date_uuid);
ALTER TABLE dim_products ADD CONSTRAINT dim_products_pk PRIMARY KEY (product_code);
ALTER TABLE dim_store_details ADD CONSTRAINT dim_store_details_pk PRIMARY KEY (store_code);
ALTER TABLE dim_users ADD CONSTRAINT dim_users_pk PRIMARY KEY (user_uuid);

ALTER TABLE orders_table ADD CONSTRAINT orders_table_fk1 FOREIGN KEY (user_uuid) REFERENCES dim_users (user_uuid);
ALTER TABLE orders_table ADD CONSTRAINT orders_table_fk2 FOREIGN KEY (card_number) REFERENCES dim_card_details (card_number);
ALTER TABLE orders_table ADD CONSTRAINT orders_table_fk3 FOREIGN KEY (store_code) REFERENCES dim_store_details (store_code);
ALTER TABLE orders_table ADD CONSTRAINT orders_table_fk4 FOREIGN KEY (product_code) REFERENCES dim_products (product_code);
ALTER TABLE orders_table ADD CONSTRAINT orders_table_fk5 FOREIGN KEY (date_uuid) REFERENCES dim_date_times (date_uuid);

