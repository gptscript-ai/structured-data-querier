import os
import tempfile

import duckdb

dbFile = tempfile.gettempdir() + '/' + os.environ['DBFILE']
duckdb.connect(database=dbFile)

print("The database has been created at " + dbFile + ".")
