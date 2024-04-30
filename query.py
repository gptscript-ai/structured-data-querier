import os
import tempfile

import duckdb

dbFile = os.getenv('DBFILE', ':memory:')
query = os.getenv('QUERY', None)

cursor = duckdb.connect(database=dbFile, config={'temp_directory': tempfile.gettempdir()})

if query is not None:
    print(cursor.sql(query).execute())
else:
    print("No query specified")
    exit(1)
