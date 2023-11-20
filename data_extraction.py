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


    def list_number_of_stores(self, endpoint):
        response = requests.get(endpoint, headers=self.headers)
        return response.json()

    def retrieve_stores_data(self, endpoint):
        num_stores = self.list_number_of_stores(endpoint)
        data = []
        for i in range(num_stores):
            store_data = requests.get(f"{endpoint}/{i}", headers=self.headers)
            data.append(store_data.json())
        return pd.DataFrame(data)