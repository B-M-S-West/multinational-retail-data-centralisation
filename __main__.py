from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector
import config


headers = {"x-api-key": config.api_key} # import the api key
db_connector = DatabaseConnector()
data_extractor = DataExtractor(headers)
data_cleaning = DataCleaning()
db_connector.init_db_engine() # initialize the database engine

def etl_user_data(db_connector, data_extractor, data_cleaning):
    user_data = data_extractor.read_rds_table(db_connector, 'legacy_users')  
    cleaned_user_data = data_cleaning.clean_user_data(user_data)
    db_creds = db_connector.read_db_creds('local_db_creds.yaml')
    db_connector.upload_to_db(cleaned_user_data, 'dim_users', db_creds)

def etl_card_data(db_connector, data_extractor, data_cleaning):
    extracted_data = data_extractor.retrieve_pdf_data("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf")
    cleaned_card_data = data_cleaning.clean_card_data(extracted_data)
    db_creds = db_connector.read_db_creds('local_db_creds.yaml')
    db_connector.upload_to_db(cleaned_card_data, 'dim_card_details', db_creds)

def etl_store_data(db_connector, data_extractor, data_cleaning):
    num_stores = data_extractor.list_number_of_stores("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores")
    data = data_extractor.retrieve_stores_data("https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details", num_stores)
    cleaned_store_data = data_cleaning.clean_store_data(data)
    db_creds = db_connector.read_db_creds('local_db_creds.yaml')
    db_connector.upload_to_db(cleaned_store_data, 'dim_store_details', db_creds)

def etl_product_data(db_connector, data_extractor, data_cleaning):
    s3_address = "s3://data-handling-public/products.csv"
    product_key = 'products.csv'
    product_information = data_extractor.extract_from_s3(s3_address, product_key)
    cleaned_product_data = data_cleaning.clean_products_data(product_information)
    product_data = data_cleaning.convert_product_weights(cleaned_product_data)
    db_creds = db_connector.read_db_creds('local_db_creds.yaml')
    db_connector.upload_to_db(product_data, 'dim_products', db_creds)

def etl_orders_data(db_connector, data_extractor, data_cleaning):
    orders_data = data_extractor.read_rds_table(db_connector, 'orders_table')  
    cleaned_orders_data = data_cleaning.clean_orders_data(orders_data)
    db_creds = db_connector.read_db_creds('local_db_creds.yaml')
    db_connector.upload_to_db(cleaned_orders_data, 'orders_table', db_creds)

def etl_events_data(db_connector, data_extractor, data_cleaning):
    date_key = 'date_details.json'
    s3_address = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'
    events_data = data_extractor.extract_from_s3_json(s3_address, date_key)
    cleaned_events_data = data_cleaning.clean_dates(events_data)
    db_creds = db_connector.read_db_creds('local_db_creds.yaml')
    db_connector.upload_to_db(cleaned_events_data, 'dim_date_times', db_creds)

# the below would run all of the above functions
etl_user_data(db_connector, data_extractor, data_cleaning)
etl_card_data(db_connector, data_extractor, data_cleaning)
etl_store_data(db_connector, data_extractor, data_cleaning)
etl_product_data(db_connector, data_extractor, data_cleaning)
etl_orders_data(db_connector, data_extractor, data_cleaning)
etl_events_data(db_connector, data_extractor, data_cleaning)