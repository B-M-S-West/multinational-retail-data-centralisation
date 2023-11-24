import pandas as pd


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
            df = df.replace('Err', pd.NA)
            return df

        @staticmethod
        def clean_store_data(df):
            df = df.dropna()
            return df

        def convert_product_weights(self, products: pd.DataFrame) -> pd.DataFrame:
            products['weight_unit'] = products['weight'].str.extract(r'(\D+)')
            products['weight'] = products['weight'].str.replace(r'[^\d\.]', '')
            products['weight'] = pd.to_numeric(products['weight'], errors='coerce')
            products['weight_unit'] = products['weight_unit'].str.lower()
            products.loc[products['weight_unit'] == 'g', 'weight'] /= 1000
            products.loc[products['weight_unit'] == 'ml', 'weight'] /= 1000
            products.drop('weight_unit', axis=1, inplace=True)
            return products

        def clean_products_data(self, products: pd.DataFrame) -> pd.DataFrame:
            products.dropna(inplace=True)
            products.drop_duplicates(inplace=True)
            products.columns = products.columns.str.lower()
            products = self.convert_product_weights(products)
            return products

        def clean_orders_data(self, df):
            df.drop(['first_name', 'last_name', '1'], axis=1, inplace=True)
            return df
