/*
This code snippet is altering the columns of the "orders_table" table. 
The "date_uuid" and "user_uuid" columns are being converted to UUID data type using the "date_uuid::UUID" and "user_uuid::UUID" expressions respectively.
The "card_number", "store_code", and "product_code" columns are being converted to VARCHAR(19), VARCHAR(11), and VARCHAR(11) data types respectively using the "column_name::VARCHAR(n)" expressions.
The "product_quantity" column is being converted to SMALLINT data type using the "product_quantity::SMALLINT" expression.
*/
ALTER TABLE orders_table ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;
ALTER TABLE orders_table ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID;
ALTER TABLE orders_table ALTER COLUMN card_number TYPE VARCHAR(19) USING card_number::VARCHAR(19);
ALTER TABLE orders_table ALTER COLUMN store_code TYPE VARCHAR(11) USING store_code::VARCHAR(11);
ALTER TABLE orders_table ALTER COLUMN product_code TYPE VARCHAR(11) USING product_code::VARCHAR(11);
ALTER TABLE orders_table ALTER COLUMN product_quantity TYPE SMALLINT USING product_quantity::SMALLINT;

/*
This code snippet is altering the columns of the "dim_users" table.
The "first_name" column is being converted to VARCHAR(255) data type using the "first_name::VARCHAR(255)" expression. 
The "last_name" column is being converted to VARCHAR(255) data type using the "last_name::VARCHAR(255)" expression.
The "date_of_birth" column is being converted to DATE data type using the "date_of_birth::DATE" expression.
The "country_code" column is being converted to VARCHAR(2) data type using the "country_code::VARCHAR(2)" expression.
The "user_uuid" column is being converted to UUID data type using the "user_uuid::UUID" expression. 
The "join_date" column is being converted to DATE data type using the "join_date::DATE" expression.
*/
ALTER TABLE dim_users ALTER COLUMN first_name TYPE VARCHAR(255) USING first_name::VARCHAR(255);
ALTER TABLE dim_users ALTER COLUMN last_name TYPE VARCHAR(255) USING last_name::VARCHAR(255);
ALTER TABLE dim_users ALTER COLUMN date_of_birth TYPE DATE USING date_of_birth::DATE;
ALTER TABLE dim_users ALTER COLUMN country_code TYPE VARCHAR(2) USING country_code::VARCHAR(2);
ALTER TABLE dim_users ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID;
ALTER TABLE dim_users ALTER COLUMN join_date TYPE DATE USING join_date::DATE;

/*
This code snippet updates the "dim_store_details" table in the database.
Sets the value of the "latitude" column to the value of the "lat" column if the "latitude" column is null.
Drops the "lat" column from the table.
Alters the data type of the "longitude" column to FLOAT using the "longitude::FLOAT" expression.
Alters the data type of the "locality" column to VARCHAR(255) using the "locality::VARCHAR(255)" expression.
Alters the data type of the "store_code" column to VARCHAR(11) using the "store_code::VARCHAR(11)" expression.
Alters the data type of the "staff_numbers" column to SMALLINT using the "staff_numbers::SMALLINT" expression.
Alters the data type of the "opening_date" column to DATE using the "opening_date::DATE" expression.
Alters the data type of the "store_type" column to VARCHAR(255) using the "store_type::VARCHAR(255)" expression.
Sets the value of the "latitude" column to NULL where the value is 'N/A'.
Alters the data type of the "latitude" column to FLOAT using the "latitude::FLOAT" expression.
Alters the data type of the "country_code" column to VARCHAR(2) using the "country_code::VARCHAR(2)" expression.
Alters the data type of the "continent" column to VARCHAR(255) using the "continent::VARCHAR(255)" expression.
*/
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

/* 
This code snippet updates the "dim_products" table in the database.
It replaces the pound sign '£' in the "product_price" column with an empty string.
It adds a new column "weight_class" of type VARCHAR(20) to the table.
It updates the "weight_class" column based on the value of the "weight" column using a CASE statement.
If the "weight" is less than 2, it sets the "weight_class" to 'Light'.
If the "weight" is between 2 and 40, it sets the "weight_class" to 'Mid_Sized'.
If the "weight" is between 40 and 140, it sets the "weight_class" to 'Heavy'.
Otherwise, it sets the "weight_class" to 'Truck_Required'.
*/
UPDATE dim_products SET product_price = REPLACE(product_price, '£', '');
ALTER TABLE dim_products ADD weight_class VARCHAR(20);
UPDATE dim_products 
SET weight_class = CASE
    WHEN weight < 2 THEN 'Light'
    WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
    WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
    ELSE 'Truck_Required'
END;

/*
This code snippet is altering the columns of the "dim_products" table. 
The "product_price" column is being converted to FLOAT data type using the "product_price::FLOAT" expression.
The "weight" column is being converted to FLOAT data type using the "weight::FLOAT" expression.
The "EAN" column is being converted to VARCHAR(255) data type using the "EAN::VARCHAR(255)" expression.
The "product_code" column is being converted to VARCHAR(11) data type using the "product_code::VARCHAR(11)" expression.
The "date_added" column is being converted to DATE data type using the "date_added::DATE" expression.
The "uuid" column is being converted to UUID data type using the "uuid::UUID" expression.
The "removed" column is being renamed to "still_available".
The "still_available" column is being converted to BOOLEAN data type using the "(still_available = 'Still_avaliable')" expression.
The "weight_class" column is being converted to VARCHAR(20) data type using the "weight_class::VARCHAR(20)" expression.
*/
ALTER TABLE dim_products ALTER COLUMN product_price TYPE FLOAT USING product_price::FLOAT;
ALTER TABLE dim_products ALTER COLUMN weight TYPE FLOAT USING weight::FLOAT;
ALTER TABLE dim_products ALTER COLUMN "EAN" TYPE VARCHAR(255) USING "EAN"::VARCHAR(255);
ALTER TABLE dim_products ALTER COLUMN product_code TYPE VARCHAR(11) USING product_code::VARCHAR(11);
ALTER TABLE dim_products ALTER COLUMN date_added TYPE DATE USING date_added::DATE;
ALTER TABLE dim_products ALTER COLUMN uuid TYPE UUID USING uuid::UUID
ALTER TABLE dim_products RENAME COLUMN removed TO still_available
ALTER TABLE dim_products ALTER COLUMN still_available TYPE BOOLEAN USING (still_available = 'Still_avaliable')
ALTER TABLE dim_products ALTER COLUMN weight_class TYPE VARCHAR(20) USING weight_class::VARCHAR(20)

/*
This code snippet is altering the columns of the "dim_date_times" table. 
The "month" column is being converted to VARCHAR(2) data type using the "month::VARCHAR(2)" expression.
The "year" column is being converted to VARCHAR(4) data type using the "year::VARCHAR(4)" expression.
The "day" column is being converted to VARCHAR(2) data type using the "day::VARCHAR(2)" expression.
The "time_period" column is being converted to VARCHAR(7) data type using the "time_period::VARCHAR(7)" expression.
The "date_uuid" column is being converted to UUID data type using the "date_uuid::UUID" expression.
*/
ALTER TABLE dim_date_times ALTER COLUMN month TYPE VARCHAR(2) USING month::VARCHAR(2);
ALTER TABLE dim_date_times ALTER COLUMN year TYPE VARCHAR(4) USING year::VARCHAR(4);
ALTER TABLE dim_date_times ALTER COLUMN day TYPE VARCHAR(2) USING day::VARCHAR(2);
ALTER TABLE dim_date_times ALTER COLUMN time_period TYPE VARCHAR(7) USING time_period::VARCHAR(7);
ALTER TABLE dim_date_times ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;

/*
This code snippet is altering the columns of the "dim_card_details" table. 
The "card_number" column is being converted to VARCHAR(22) data type using the "card_number::VARCHAR(22)" expression.
The "expiry_date" column is being converted to VARCHAR(10) data type using the "expiry_date::VARCHAR(10)" expression.
The "date_payment_confirmed" column is being converted to DATE data type using the "date_payment_confirmed::DATE" expression.
*/
ALTER TABLE dim_card_details ALTER COLUMN card_number TYPE VARCHAR(22) USING card_number::VARCHAR(22);
ALTER TABLE dim_card_details ALTER COLUMN expiry_date TYPE VARCHAR(10) USING expiry_date::VARCHAR(10);
ALTER TABLE dim_card_details ALTER COLUMN date_payment_confirmed TYPE DATE USING date_payment_confirmed::DATE;

/*
This code snippet adds primary key constraints to the specified columns in their respective tables. 
For the "dim_card_details" table, the "card_number" column is set as the primary key.
For the "dim_date_times" table, the "date_uuid" column is set as the primary key.
For the "dim_products" table, the "product_code" column is set as the primary key.
For the "dim_store_details" table, the "store_code" column is set as the primary key.
For the "dim_users" table, the "user_uuid" column is set as the primary key.
*/
ALTER TABLE dim_card_details ADD CONSTRAINT dim_card_details_pk PRIMARY KEY (card_number);
ALTER TABLE dim_date_times ADD CONSTRAINT dim_date_times_pk PRIMARY KEY (date_uuid);
ALTER TABLE dim_products ADD CONSTRAINT dim_products_pk PRIMARY KEY (product_code);
ALTER TABLE dim_store_details ADD CONSTRAINT dim_store_details_pk PRIMARY KEY (store_code);
ALTER TABLE dim_users ADD CONSTRAINT dim_users_pk PRIMARY KEY (user_uuid);

/*
This code snippet adds foreign key constraints to the "orders_table" table. 
The "user_uuid" column is set as a foreign key referencing the "user_uuid" column in the "dim_users" table.
The "card_number" column is set as a foreign key referencing the "card_number" column in the "dim_card_details" table.
The "store_code" column is set as a foreign key referencing the "store_code" column in the "dim_store_details" table.
The "product_code" column is set as a foreign key referencing the "product_code" column in the "dim_products" table.
The "date_uuid" column is set as a foreign key referencing the "date_uuid" column in the "dim_date_times" table.
*/
ALTER TABLE orders_table ADD CONSTRAINT orders_table_fk1 FOREIGN KEY (user_uuid) REFERENCES dim_users (user_uuid);
ALTER TABLE orders_table ADD CONSTRAINT orders_table_fk2 FOREIGN KEY (card_number) REFERENCES dim_card_details (card_number);
ALTER TABLE orders_table ADD CONSTRAINT orders_table_fk3 FOREIGN KEY (store_code) REFERENCES dim_store_details (store_code);
ALTER TABLE orders_table ADD CONSTRAINT orders_table_fk4 FOREIGN KEY (product_code) REFERENCES dim_products (product_code);
ALTER TABLE orders_table ADD CONSTRAINT orders_table_fk5 FOREIGN KEY (date_uuid) REFERENCES dim_date_times (date_uuid);

