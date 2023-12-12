import boto3
from botocore import UNSIGNED
from botocore.config import Config
import json
import pandas as pd
import requests
import tabula


class DataExtractor:


    def read_rds_table(self, DatabaseConnector, table_name):
        """
        Read data from an RDS table.

        Parameters:
            DatabaseConnector (object): An instance of the DatabaseConnector class.
            table_name (str): The name of the table to read.

        Returns:
            pandas.DataFrame: The data read from the table.
        """
        engine = DatabaseConnector.init_db_engine() 
        data = pd.read_sql_table(table_name, engine)
        return data    

    def retrieve_pdf_data(self, link):
        """
        Read data from an RDS table.

        Parameters:
            DatabaseConnector (object): An instance of the DatabaseConnector class.
            table_name (str): The name of the table to read.

        Returns:
            pandas.DataFrame: The data read from the table.
        """
        dfs = tabula.read_pdf(link, pages='all')
        df = pd.concat(dfs)
        return df

    def __init__(self, headers):
        """
        Initializes an instance of the class with the given headers.

        :param headers: The headers for the instance.
        """
        self.headers = headers

    def list_number_of_stores(self, endpoint):
        """
        Initializes an instance of the class with the given headers.

        :param headers: The headers for the instance.
        """
        response = requests.get(endpoint, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response Text: {response.text}")

    def retrieve_stores_data(self, endpoint, num_stores):
        """
        Initializes an instance of the class with the given headers.

        :param headers: The headers for the instance.
        """
        number_of_stores = num_stores['number_stores']
        data = []
        for i in range(number_of_stores):
            store_data = requests.get(f"{endpoint}/{i}", headers=self.headers)
            data.append(store_data.json())
        return pd.DataFrame(data)

    def extract_from_s3(self, s3_address: str, key) -> pd.DataFrame:
        """
        Initializes an instance of the class with the given headers.

        :param headers: The headers for the instance.
        """
        s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
        obj = s3.get_object(Bucket='data-handling-public', Key=key)
        df = pd.read_csv(obj['Body'])
        return df

    def extract_from_s3_json(self, s3_address: str, key):
        """
        Extracts data from a JSON file stored on an S3 bucket.

        Args:
            s3_address (str): The address of the S3 bucket.
            key: The key of the JSON file within the S3 bucket.

        Returns:
            df (pandas.DataFrame): The extracted data as a pandas DataFrame.
        """
        s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
        obj = s3.get_object(Bucket='data-handling-public', Key=key)
        file_content = obj.get('Body').read().decode('utf-8')
        json_content = json.loads(file_content)
        df = pd.DataFrame(json_content)
        return df
