import os
import tempfile

import duckdb

dbFile = tempfile.gettempdir() + '/' + os.environ['DBFILE']

if dbFile is None:
    print("Error, Please provide a database file.")
    exit(1)
if not os.path.exists(dbFile):
    duckdb.connect(database=dbFile)
    print("The database has been created at " + dbFile + ".")
else:
    print("The database already exists at " + dbFile + ".")