#!/usr/bin/env python

# This script exports all of the tables in the PUDL SQLite database into 
# separate CSV files.

# This script depends on the environment variable PUDL_DIR being set
# to the directory containing a pudl.sqlite file; pudl.sqlite is the
# SQLite version of the PUDL database, which can be found at the 
# bottom of this page:  https://data.catalyst.coop/pudl .
# There also must be subdirectory of that directory named csv where a CSV file
#  for every PUDL table will be stored.

import sqlite3
import pandas as pd
import os

pudl_dir = os.environ['PUDL_DIR']

# Connect to the SQLite database
conn = sqlite3.connect(os.path.join(pudl_dir, 'pudl.sqlite'))

# Get the cursor object
cursor = conn.cursor()

# Get the list of tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# For each table, convert to CSV and save
for table_name in tables:
    table_name = table_name[0]
    print(table_name)
    table = pd.read_sql_query(f"SELECT * from {table_name}", conn)
    table.to_csv(os.path.join(pudl_dir, 'csv', table_name + '.csv'), index_label='index')

# Close the connection
conn.close()
