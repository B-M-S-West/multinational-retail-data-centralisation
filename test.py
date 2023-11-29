from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector
import uuid

headers = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}

db_connector = DatabaseConnector()
data_extractor = DataExtractor(headers)
data_cleaning = DataCleaning()

# Connect and read the database
db_connector.init_db_engine()
db_creds = db_connector.read_db_creds('local_db_creds.yaml')

# Extract the information from the pdf link
extracted_data = data_extractor.retrieve_pdf_data("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf")
cleaned_card_data = data_cleaning.clean_card_data(extracted_data)

# Upload the cleaned card data to the 'dim_card_details
db_connector.upload_to_db(cleaned_card_data, 'dim_card_details', db_creds['RDS_DATABASE'], db_creds['RDS_USER'], db_creds['RDS_PASSWORD'], db_creds['RDS_HOST'], db_creds['RDS_PORT'])
