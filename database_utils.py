import yaml
from sqlalchemy import create_engine
from sqlalchemy import inspect


class DatabaseConnector:
    '''
    This class uses the credentials in db_creds.yaml 
    to create a dictionary containing the credentials
    @staticmethod decorator used as this method belongs to the class. 
    '''


    @staticmethod
    def read_db_creds(file_name):
        with open(file_name, 'r') as file:
            db_creds = yaml.safe_load(file)
        return db_creds


    @staticmethod
    def init_db_engine():
        db_creds = DatabaseConnector.read_db_creds('db_creds.yaml')
        engine = create_engine(f"postgresql://{db_creds['RDS_USER']}:{db_creds['RDS_PASSWORD']}@{db_creds['RDS_HOST']}:{db_creds['RDS_PORT']}/{db_creds['RDS_DATABASE']}")
        return engine
    

    @staticmethod
    def list_db_tables():
        engine = DatabaseConnector.init_db_engine()
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        return table_names


    @classmethod
    def upload_to_db(cls, df, table_name, db_name, db_user, db_password, db_host, db_port):
        engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
        df.to_sql(table_name, engine, if_exists='replace', index=False)