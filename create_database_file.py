import os

import duckdb

dbFile = os.environ['GPTSCRIPT_WORKSPACE_DIR'] + '/' + os.environ['DBFILE']

if dbFile is None:
    print("Error, Please provide a database file.")
    exit(1)
if not os.path.exists(dbFile):
    duckdb.connect(database=dbFile)
    print("Success, The database has been created at " + dbFile + ".")
else:
    print("Success, The database already exists at " + dbFile + ".")
