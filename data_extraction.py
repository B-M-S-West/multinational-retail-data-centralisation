import pandas as pd
import tabula
from database_utils import DatabaseConnector


class DataExtractor:


    def read_rds_table(self, DatabaseConnector, table_name):
        engine = DatabaseConnector.init_db_engine() 
        data = pd.read_sql_table(table_name, engine)
        return data
    

    def retrieve_pdf_data(self, link):
        dfs = tabula.read_pdf(link, pages='all')
        df = pd.concat(dfs)
        return df