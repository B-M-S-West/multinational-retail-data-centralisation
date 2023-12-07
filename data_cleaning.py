from wsgiref.types import ErrorStream
import pandas as pd
import numpy as np

class DataCleaning:


        def clean_user_data(self, df):
            df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')
            df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')
            df["address"] = df["address"].str.replace('\W', ' ', regex=True)
            df['country_code'] = df['country_code'].replace('GGB', 'GB')
            df.dropna(how='all')
            return df

        def clean_card_data(self, df):
            df['date_payment_confirmed'] = pd.to_datetime(df['date_payment_confirmed'], errors='coerce')
            df['card_number'] = df['card_number'].astype(str)
            df['card_number'] = df['card_number'].str.replace('\W', '', regex=True)
            df['card_number'] = df['card_number'].apply(lambda x: np.nan if x=='NULL' else x)
            df.dropna(subset=['card_number'], inplace=True)
            return df

        def clean_store_data(self, df):
            df['opening_date'] = pd.to_datetime(df['opening_date'], errors='coerce')
            df['index'] = pd.to_numeric(df['index'], errors='coerce')
            df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
            df['address'] = df['address'].str.replace(r'\n', ' ', regex=True)
            df['continent'] = df['continent'].replace(r'ee', '', regex=True)
            df['staff_numbers'] = df['staff_numbers'].replace(r'\D+', '', regex=True)
            df['address'] = df['address'].str.strip()
            df = df[df['country_code'].str.len()<=2]
            return df

        def convert_product_weights(self, products: pd.DataFrame) -> pd.DataFrame:
            products['weight_unit'] = products['weight'].str.extract('([a-zA-Z]+)')
            products['weight'] = products['weight'].str.extract('(\d+\.?\d*)')
            products['weight'] = pd.to_numeric(products['weight'], errors='coerce')
            products['weight_unit'] = products['weight_unit'].str.lower()
            products.loc[products['weight_unit'] == 'g', 'weight'] /= 1000
            products.loc[products['weight_unit'] == 'ml', 'weight'] /= 1000
            products.drop('weight_unit', axis=1, inplace=True)
            return products

        def clean_products_data(self, products: pd.DataFrame) -> pd.DataFrame:
            products['date_added'] = pd.to_datetime(products['date_added'], errors='coerce')
            products['product_code'] = products['product_code'].str.upper()
            products.dropna(how='all') # need to change to drop based upon two columns being null and remove random text rows
            return products

        def clean_orders_data(self, df):
            df.drop(['level_0', 'first_name', 'last_name', '1'], axis=1, inplace=True)
            return df
        
        def clean_dates(self, df):
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce', format='%H:%M:%S')
            df.drop_duplicates(subset=['date_uuid'], keep='first', inplace=True)
            df.dropna(subset=['day', 'year', 'month'], inplace=True)
            df = df[df['month'].str.len()<=2]
            return df
