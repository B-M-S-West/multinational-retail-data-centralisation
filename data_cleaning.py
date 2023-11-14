import pandas as pd


class DataCleaning:
    # Make a copy of the DataFrame to avoid modifying the original data
        
        def clean_user_data(self, df):
            df_clean = df.copy()

            # Replace NULL values with appropriate replacements
            # Numerical columns NULL values replaced with mean values
            # Categorical columns NULL values replaced with the most common category
            for col in df_clean.columns:
                if pd.api.types.is_numeric_dtype(df_clean[col]):
                    df_clean[col].fillna(df_clean[col].mean(), inplace=True)
                elif pd.api.types.is_string_dtype(df_clean[col]):
                    df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)

            # Correct errors with dates. Converting a date column to datetime format
            df_clean['date_of_birth'] = pd.to_datetime(df_clean['date_of_birth'], errors='coerce')
            df_clean['join_date'] = pd.to_datetime(df_clean['join_date'], errors='coerce')

            # Removes the NULL values
            df_clean = df_clean.dropna()

            return df_clean