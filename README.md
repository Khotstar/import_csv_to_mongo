# import csv file to mongodb

## Setup 
pip install -r requirements.txt

## Method
import_csv(file_path,  override=True, collection_name=None)

import_csv method imports the CSV file to mongodb, if collection name is not specified it will create collection name
same as the CSV file name.
By default collection will be dropped if exists and new collection will be created.
If override is set to False it will append the records to existing collection.

# Configure MongoDb In import_csv_to_mongo.py
- MONGO_SERVER_URL = 'localhost'
- MONGO_SERVER_PORT = 27017
- MONGO_USER_NAME = 'root'
- MONGO_PASSWORD = 'hupstore123'
- MONGO_DB_NAME = 'db'

- Import CSV file to MongoDb using commandline 
 python import_csv_to_mongo.py <File name>.csv
 E.g:  python import_csv_to_mongo.py Groceries_dataset.csv
 
# Note
- Code is implemented using Python 3.7
