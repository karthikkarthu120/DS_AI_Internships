import sqlite3
import pandas as pd

conn = sqlite3.connect("C:/SQL Lite/internship.db")
df=pd.read_sql_query("SELECT * FROM interns", conn)
print("All data Retreived :\n",df)

nt=pd.read_sql_query("select name,track from interns",conn)
print("\nOnly name and track: \n",nt)