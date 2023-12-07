from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector
import uuid

headers = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}

db_connector = DatabaseConnector()
data_extractor = DataExtractor(headers)
data_cleaning = DataCleaning()

# Extract and clean the user data
user_data = data_extractor.read_rds_table(db_connector, 'legacy_users')  
cleaned_user_data = data_cleaning.clean_user_data(user_data)

# Upload the cleaned user data to the 'dim_users' table
db_creds = db_connector.read_db_creds('local_db_creds.yaml')
db_connector.upload_to_db(cleaned_user_data, 'dim_users', db_creds['RDS_DATABASE'], db_creds['RDS_USER'], db_creds['RDS_PASSWORD'], db_creds['RDS_HOST'], db_creds['RDS_PORT'])

# Extract product information from s3_address
s3_address = "s3://data-handling-public/products.csv"
product_key = 'products.csv'
product_information = data_extractor.extract_from_s3(s3_address, product_key)

# Clean the product information before uploading
cleaned_product_data = data_cleaning.clean_products_data(product_information)
product_data = data_cleaning.convert_product_weights(cleaned_product_data)

# Upload the cleaned product data to the 'dim_products
db_connector.upload_to_db(product_data, 'dim_products', db_creds['RDS_DATABASE'], db_creds['RDS_USER'], db_creds['RDS_PASSWORD'], db_creds['RDS_HOST'], db_creds['RDS_PORT'])
