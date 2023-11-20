from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector


db_connector = DatabaseConnector()
data_extractor = DataExtractor()
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

headers = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
data = data_extractor.retrieve_stores_data("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details")
cleaned_store_data = data_cleaner.clean_store_data(data)


# Upload the cleaned card data to the 'dim_card_details
db_connector.upload_to_db(cleaned_store_data, 'dim_store_details', db_creds['RDS_DATABASE'], db_creds['RDS_USER'], db_creds['RDS_PASSWORD'], db_creds['RDS_HOST'], db_creds['RDS_PORT'])