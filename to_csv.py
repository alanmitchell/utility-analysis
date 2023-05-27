#!/usr/bin/env python
import sqlite3
import pandas as pd
import os

# Connect to the SQLite database
conn = sqlite3.connect('pudl.sqlite') 

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
    table.to_csv(os.path.join('csv/', table_name + '.csv'), index_label='index')

# Close the connection
conn.close()
