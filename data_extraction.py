import requests
import boto3
from botocore import UNSIGNED
from botocore.config import Config
import pandas as pd
import tabula


class DataExtractor:


    def read_rds_table(self, DatabaseConnector, table_name):
        engine = DatabaseConnector.init_db_engine() 
        data = pd.read_sql_table(table_name, engine)
        return data    


    def retrieve_pdf_data(self, link):
        dfs = tabula.read_pdf(link, pages='all')
        df = pd.concat(dfs)
        return df


    def __init__(self, headers):
        self.headers = headers

    def list_number_of_stores(self, endpoint):
        response = requests.get(endpoint, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response Text: {response.text}")


    def retrieve_stores_data(self, endpoint, num_stores):
        number_of_stores = num_stores['number_stores']
        data = []
        for i in range(number_of_stores):
            store_data = requests.get(f"{endpoint}/{i}", headers=self.headers)
            data.append(store_data.json())
        return pd.DataFrame(data)


    def extract_from_s3(self, s3_address: str) -> pd.DataFrame:
        s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
        obj = s3.get_object(Bucket='data-handling-public', Key='products.csv')
        df = pd.read_csv(obj['Body'])
        return df
        