import os
import tempfile
import time

import duckdb

dbFile = os.getenv('DBFILE', None)
if dbFile is None:
    print("Error, Please provide a database file.")
    exit(0)
if not os.path.exists(dbFile):
    print("Error, Database does not exist.")
    exit(0)
query = os.getenv('QUERY', None)
readonly = os.getenv('READONLY', 'false').lower() == 'true'

max_retries = 10
attempts = 0
success = False

while not success and attempts < max_retries:
        try:
            cursor = duckdb.connect(database=dbFile, read_only=readonly, config={'temp_directory': tempfile.gettempdir()})
            success = True
        except:
            time.sleep(1)
            attempts += 1

if success:
    if query is not None:
        try:
            result = cursor.sql(query)
        except Exception as e:
            print(f"Error: {e}, please reformulate your query and try again")
            exit(0)
        if result is not None:
            result.show(max_rows=10000000, max_width=10000000)
        else:
            print("Query returned no results, please try another query.")
            exit(0)

    else:
        print("No query specified")
        exit(1)
else:
    print("Failed to connect to database")
    exit(1)