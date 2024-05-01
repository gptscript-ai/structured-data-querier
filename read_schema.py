import os
import tempfile

import duckdb

dbFile = os.getenv('DBFILE', None)
if dbFile is None:
    print("Error, Please provide a database file.")
    exit(1)
filePath = os.getenv('FILEPATH', None)
if filePath is None:
    print("Error, Please provide a file path.")
    exit(1)
if not os.path.exists(filePath):
    print("Error, File does not exist.")
    exit(1)

cursor = duckdb.connect(database=dbFile, config={'temp_directory': tempfile.gettempdir()})

file = os.path.basename(filePath)
file_name, file_extension = os.path.splitext(file)
if file_extension == '.csv':
    schema_query = f"CREATE TABLE IF NOT EXISTS {file_name} AS SELECT * FROM read_csv_auto('{filePath}');"
elif file_extension == '.xlsx':
    cursor.install_extension("spatial")
    cursor.load_extension("spatial")
    schema_query = f"CREATE TABLE IF NOT EXISTS {file_name} AS SELECT * FROM st_read('{filePath}', open_options=['HEADERS=FORCE']);"
else:
    print("Error, Unsupported file type. Please provide a .csv or .xlsx file.")
    exit(1)

cursor.execute(schema_query)

query = f"PRAGMA table_info('{file_name}');"
print(f"Schema for table '{file_name}':")
print(cursor.sql(query).execute())

