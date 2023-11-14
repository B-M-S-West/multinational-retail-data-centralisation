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