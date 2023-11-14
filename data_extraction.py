import pandas as pd
from database_utils import DatabaseConnector


class DataExtractor:


    def read_rds_table(self, DatabaseConnector, table_name):
        engine = DatabaseConnector.init_db_engine() 
        data = pd.read_sql_table(table_name, engine)
        return data