import pandas as pd
import numpy as np

class DataCleaning:
    # Make a copy of the DataFrame to avoid modifying the original data


        def clean_user_data(self, df):
            df_clean = df.copy()

            # Correct errors with dates. Converting a date column to datetime format
            df_clean['date_of_birth'] = pd.to_datetime(df_clean['date_of_birth'], errors='coerce')
            df_clean['join_date'] = pd.to_datetime(df_clean['join_date'], errors='coerce')

            # Removes the NULL values
            df_clean = df_clean.dropna()
            return df_clean

        def clean_card_data(self, df):
            df = df.dropna()
            df = df[df['date_payment_confirmed'] != 'NULL']
            df = df[df['expiry_date'].str.len() <= 6]
            df = df.replace('Err', pd.NA)
            return df

        @staticmethod
        def clean_store_data(df):
            df['opening_date'] = pd.to_datetime(df['opening_date'], errors='coerce')
            df = df.dropna(subset=['opening_date'])
            df['staff_numbers'] = df['staff_numbers'].replace('[^0-9]', '', regex=True)
            df = df.replace('N/A', np.nan)
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
            products.dropna(inplace=True)
            products.drop_duplicates(inplace=True)
            products = products[~products['product_price'].str.contains('[a-zA-Z]')]
            return products

        def clean_orders_data(self, df):
            df.drop(['first_name', 'last_name', '1'], axis=1, inplace=True)
            return df
        
        def clean_dates(self, df):
            df = df[df['month'].str.len() <= 4]
            df = df[df['date_uuid'] != 'NULL']
            return df
