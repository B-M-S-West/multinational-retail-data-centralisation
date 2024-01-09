import pandas as pd
import numpy as np

class DataCleaning:


        def clean_user_data(self, df):
            """
            Cleans the user data by performing the following operations:

            1. Converts the 'date_of_birth' column to datetime format with 'coerce' option.
            2. Converts the 'join_date' column to datetime format with 'coerce' option.
            3. Replaces any non-word characters in the 'address' column with a space.
            4. Replaces 'GGB' with 'GB' in the 'country_code' column.
            5. Filters the DataFrame to include only rows where the length of 'user_uuid' is greater than or equal to 12.

            Parameters:
            - df (DataFrame): The input DataFrame containing the user data.

            Returns:
            - df (DataFrame): The cleaned DataFrame with the specified transformations applied.
            """
            #NOTE: Sama as extractor, your readability here is brilliant!
            df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')
            df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')
            df["address"] = df["address"].str.replace('\W', ' ', regex=True)
            df['country_code'] = df['country_code'].replace('GGB', 'GB')
            df = df[df['user_uuid'].str.len()>=12]
            return df

        def clean_card_data(self, df):
            """
            Cleans the card data in the given DataFrame.

            Parameters:
                df (pandas.DataFrame): The DataFrame containing the card data.

            Returns:
                pandas.DataFrame: The cleaned DataFrame.
            """
            df['date_payment_confirmed'] = pd.to_datetime(df['date_payment_confirmed'], errors='coerce')
            df['card_number'] = df['card_number'].astype(str)
            #NOTE: This specific transformation below promotes reusability, keep this up!
            df['card_number'] = df['card_number'].str.replace('\W', '', regex=True)
            df['card_number'] = df['card_number'].apply(lambda x: np.nan if x=='NULL' else x)
            df.dropna(subset=['card_number'], inplace=True)
            return df

        def clean_store_data(self, df):
            """
            Clean the store data by performing the following operations:
            
            - Convert the 'opening_date' column to datetime format.
            - Convert the 'index' column to numeric format.
            - Convert the 'longitude' column to numeric format.
            - Replace newline characters in the 'address' column with spaces.
            - Remove the substring 'ee' from the 'continent' column.
            - Remove all non-digit characters from the 'staff_numbers' column.
            - Remove leading and trailing whitespace from the 'address' column.
            - Filter rows where the length of 'country_code' is greater than 2.
            
            Parameters:
            - df: DataFrame containing the store data.
            
            Returns:
            - df: Cleaned DataFrame.
            """
            df['opening_date'] = pd.to_datetime(df['opening_date'], errors='coerce')
            df['index'] = pd.to_numeric(df['index'], errors='coerce')
            df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
            #NOTE: Loving the regex used throughout these cleaning methods!
            df['address'] = df['address'].str.replace(r'\n', ' ', regex=True)
            df['continent'] = df['continent'].replace(r'ee', '', regex=True)
            df['staff_numbers'] = df['staff_numbers'].replace(r'\D+', '', regex=True)
            df['address'] = df['address'].str.strip()
            df = df[df['country_code'].str.len()<=2]
            return df

        def convert_product_weights(self, products: pd.DataFrame) -> pd.DataFrame:
            #NOTE: Defining methods using type hints & expected returns is perfect here!
            """
            Converts the weights of products from different units to a uniform unit.

            Args:
                products (pd.DataFrame): The DataFrame containing the products and their weights.

            Returns:
                pd.DataFrame: The updated DataFrame with the weights converted to a uniform unit.
            """
            products['weight_unit'] = products['weight'].str.extract('([a-zA-Z]+)')
            products['weight'] = products['weight'].str.extract('(\d+\.?\d*)')
            products['weight'] = pd.to_numeric(products['weight'], errors='coerce')
            products['weight_unit'] = products['weight_unit'].str.lower()
            products.loc[products['weight_unit'] == 'g', 'weight'] /= 1000
            products.loc[products['weight_unit'] == 'ml', 'weight'] /= 1000
            products.drop('weight_unit', axis=1, inplace=True)
            return products

        def clean_products_data(self, products: pd.DataFrame) -> pd.DataFrame:
            """
            Clean the products data by performing the following operations:
            
            - Convert the 'date_added' column to datetime format.
            - Convert the 'product_code' column to uppercase.
            - Drop rows with missing values in the 'uuid' column.
            - Keep only rows where the length of the 'uuid' column is greater than or equal to 12.
            
            Parameters:
            - products (pd.DataFrame): The input dataframe containing the products data.
            
            Returns:
            - pd.DataFrame: The cleaned products dataframe.
            """
            products['date_added'] = pd.to_datetime(products['date_added'], errors='coerce')
            products['product_code'] = products['product_code'].str.upper()
            products.dropna(subset = ['uuid'], inplace=True)
            products = products[products['uuid'].str.len()>=12]
            return products

        def clean_orders_data(self, df):
            """
            Cleans the orders data by dropping unnecessary columns and converting the 'product_code' column to uppercase.
            
            Parameters:
            - df (pandas.DataFrame): The input dataframe containing the orders data.
            
            Returns:
            - df (pandas.DataFrame): The cleaned dataframe.
            """
            df.drop(['level_0', 'first_name', 'last_name', '1'], axis=1, inplace=True)
            df['product_code'] = df['product_code'].str.upper()
            return df
        
        @staticmethod
        def clean_dates(df):
            """
            Cleans the dates in the given DataFrame.

            Parameters:
                df (pandas.DataFrame): The DataFrame containing the dates.

            Returns:
                pandas.DataFrame: The cleaned DataFrame with the dates.
            """
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce', format='%H:%M:%S')
            df.drop_duplicates(subset=['date_uuid'], keep='first', inplace=True)
            df.dropna(subset=['day', 'year', 'month'], inplace=True)
            df = df[df['month'].str.len()<=2]
            return df
