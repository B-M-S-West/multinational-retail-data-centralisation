from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector

headers = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}

db_connector = DatabaseConnector()
data_extractor = DataExtractor(headers)
data_cleaning = DataCleaning()

# Connect and read the database
db_connector.init_db_engine()

