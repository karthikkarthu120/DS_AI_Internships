import sqlite3
import pandas as pd

conn = sqlite3.connect("C:\SQL Lite\AIML_Karthik.db")
df = pd.read_sql_query("SELECT * FROM students", conn)
print(df)