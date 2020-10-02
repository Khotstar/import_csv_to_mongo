import sys
import pandas as pd
import pymongo
import json

# Configuration for MONGO DB
MONGO_SERVER_URL = 'localhost'
MONGO_SERVER_PORT = 27017
MONGO_USER_NAME = 'root'
MONGO_PASSWORD = 'hupstore123'
MONGO_DB_NAME = 'db'


def import_csv(file_path,  override=True, collection_name=None):
    """
        Imports csv file to mongo db
        Parameters
        ----------
        file_path : str
            csv file path including the file name and extension
        override: boolean
            Default True, if true it will drop existing collection and create an new one
            If False then it will append csv file records to existing collection
        collection_name: str
            Default None: if specified then it will be used as collection name


    """
    if not file_path:
        print("Missing file_path")
        return

    try:
        mongo_client = get_monog_client()
        mongo_db = mongo_client[MONGO_DB_NAME]
        collection_name = collection_name if collection_name else get_collection_name_from_file_path(file_path)
        
        df = pd.read_csv(file_path)
        data_json = json.loads(df.to_json(orient='records'))
        db_cm = mongo_db[collection_name]
        if override:
            db_cm.drop()

        db_cm.insert_many(data_json)
        print(f'CSV file import completed,and data is availabe in  Collection {collection_name}')
    except Exception as e:
        print(f'Error While importing {file_path}: {e}')
    

def get_monog_client():
    try:
        mongo_url = f'mongodb://{MONGO_USER_NAME}:{MONGO_PASSWORD}@{MONGO_SERVER_URL}:{MONGO_SERVER_PORT}'
        return pymongo.MongoClient(mongo_url, MONGO_SERVER_PORT)
    except Exception as e:
        print(f'Error While connection MongoDb: {e}')
        raise e


def get_collection_name_from_file_path(file_path):
    return (file_path.split('/'))[-1].split('.')[0]


if __name__ == '__main__':
    file_path = sys.argv[1]
    if not file_path:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    import_csv(file_path)