from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector

headers = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}

db_connector = DatabaseConnector()
data_extractor = DataExtractor(headers)
data_cleaning = DataCleaning()

# Connect and read the database
db_connector.init_db_engine()

# Extract and clean the user data
user_data = data_extractor.read_rds_table(db_connector, 'legacy_users')  
cleaned_user_data = data_cleaning.clean_user_data(user_data)

# Upload the cleaned user data to the 'dim_users' table
db_creds = db_connector.read_db_creds('local_db_creds.yaml')
db_connector.upload_to_db(cleaned_user_data, 'dim_users', db_creds['RDS_DATABASE'], db_creds['RDS_USER'], db_creds['RDS_PASSWORD'], db_creds['RDS_HOST'], db_creds['RDS_PORT'])

# Extract the information from the pdf link
extracted_data = data_extractor.retrieve_pdf_data("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf")
cleaned_card_data = data_cleaning.clean_card_data(extracted_data)

# Upload the cleaned card data to the 'dim_card_details
db_connector.upload_to_db(cleaned_card_data, 'dim_card_details', db_creds['RDS_DATABASE'], db_creds['RDS_USER'], db_creds['RDS_PASSWORD'], db_creds['RDS_HOST'], db_creds['RDS_PORT'])

# Number of stores and then extract the stores data
num_stores = data_extractor.list_number_of_stores("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores")
data = data_extractor.retrieve_stores_data("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details", num_stores)

# Clean the stores data before uploading
cleaned_store_data = data_cleaning.clean_store_data(data)

# Upload the cleaned store details to the 'dim_store_details
db_connector.upload_to_db(cleaned_store_data, 'dim_store_details', db_creds['RDS_DATABASE'], db_creds['RDS_USER'], db_creds['RDS_PASSWORD'], db_creds['RDS_HOST'], db_creds['RDS_PORT'])

# Extract product information from s3_address
s3_address = "s3://data-handling-public/products.csv"
product_key = 'products.csv'
product_information = data_extractor.extract_from_s3(s3_address, product_key)

# Clean the product information before uploading
cleaned_product_data = data_cleaning.clean_products_data(product_information)
product_data = data_cleaning.convert_product_weights(cleaned_product_data)

# Upload the cleaned product data to the 'dim_products
db_connector.upload_to_db(product_data, 'dim_products', db_creds['RDS_DATABASE'], db_creds['RDS_USER'], db_creds['RDS_PASSWORD'], db_creds['RDS_HOST'], db_creds['RDS_PORT'])

# Extract and clean the orders data
orders_data = data_extractor.read_rds_table(db_connector, 'orders_table')  
cleaned_orders_data = data_cleaning.clean_orders_data(orders_data)

# Upload the cleaned orders data to the 'orders_table' table
db_connector.upload_to_db(cleaned_orders_data, 'orders_table', db_creds['RDS_DATABASE'], db_creds['RDS_USER'], db_creds['RDS_PASSWORD'], db_creds['RDS_HOST'], db_creds['RDS_PORT'])

# Extracting date events data
date_key = 'date_details.json'
s3_address = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'
events_data = data_extractor.extract_from_s3_json(s3_address, date_key)

# clean the dates
cleaned_events_data = data_cleaning.clean_dates(events_data)

# Upload the cleaned events data to the 'dim_date_times' table
db_connector.upload_to_db(cleaned_events_data, 'dim_date_times', db_creds['RDS_DATABASE'], db_creds['RDS_USER'], db_creds['RDS_PASSWORD'], db_creds['RDS_HOST'], db_creds['RDS_PORT'])