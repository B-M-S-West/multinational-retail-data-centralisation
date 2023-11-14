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

# Upload the cleaned data to the 'dim_users' table
db_creds = db_connector.read_db_creds('local_db_creds.yaml')
db_connector.upload_to_db(cleaned_user_data, 'dim_users', db_creds['RDS_DATABASE'], db_creds['RDS_USER'], db_creds['RDS_PASSWORD'], db_creds['RDS_HOST'], db_creds['RDS_PORT'])