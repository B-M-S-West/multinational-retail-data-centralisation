from sqlalchemy import create_engine
from sqlalchemy import inspect
import yaml


class DatabaseConnector:


    @staticmethod
    def read_db_creds(file_name):
        """
        Reads the database credentials from a given file.

        Args:
            file_name (str): The name of the file containing the database credentials.

        Returns:
            dict: A dictionary containing the database credentials.

        """
        with open(file_name, 'r') as file:
            db_creds = yaml.safe_load(file)
        return db_creds

    @staticmethod
    def init_db_engine():
        """
        Initializes the database engine.

        Returns:
            sqlalchemy.engine.Engine: The database engine.
        """
        db_creds = DatabaseConnector.read_db_creds('db_creds.yaml')
        engine = create_engine(f"postgresql://{db_creds['RDS_USER']}:{db_creds['RDS_PASSWORD']}@{db_creds['RDS_HOST']}:{db_creds['RDS_PORT']}/{db_creds['RDS_DATABASE']}")
        return engine

    @staticmethod
    def list_db_tables():
        """
        Retrieves a list of all the tables in the database.

        :return: A list of strings representing the names of all the tables in the database.
        """
        engine = DatabaseConnector.init_db_engine()
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        return table_names

    @classmethod
    def upload_to_db(cls, df, table_name, db_name, db_user, db_password, db_host, db_port):
        """
        Uploads a DataFrame to a PostgreSQL database table.

        Args:
            df (pandas.DataFrame): The DataFrame to be uploaded.
            table_name (str): The name of the table to upload the DataFrame to.
            db_name (str): The name of the database.
            db_user (str): The username for the database.
            db_password (str): The password for the database.
            db_host (str): The host address of the database.
            db_port (str): The port number of the database.

        Returns:
            None
        """
        engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
        df.to_sql(table_name, engine, if_exists='replace', index=False)
