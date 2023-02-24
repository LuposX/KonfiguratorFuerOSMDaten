## About the File

The file originates from the website taginfo which tracks all used tags in openstreetmap.
Fore more information check out their wiki on their API.

## Creation Process

The file which has all used osm keys in it, is used for the recommender sytsem to recommend keys to the 
user while he types.
To Create the file which has all used osm keys in it I did the following:
- Download the key database with the name "taginfo-chronology.db.bz2"
from the website taginfo.openstreetmap(https://taginfo.openstreetmap.org/download)
- Than I created a python script which transformed the databse into a .csv the database is saved in the sqlite format
look below to check the code.

## Script Databsse to csv

```python
import sqlite3
import pandas as pd

# Create a SQL connection to our SQLite database
con = sqlite3.connect("taginfo_chronology.db")

# get all tables in db
sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
cursor = con.cursor()
cursor.execute(sql_query)
print(cursor.fetchall())

# get the key database 
df = pd.read_sql_query("SELECT * FROM keys_chronology", con)
print(len(df))

# remove not needed columns
df_dropped = df.drop(columns=["data", "first_use", "smoothness"])
df_dropped.head()

# save the database.
df_dropped.to_csv("all_osm_keys.csv")
``