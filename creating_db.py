import pandas as pd
import sqlite3

csv_file_path = "lag_data_new.csv"
data = pd.read_csv("lag_data_new.csv")
database = "synthesis.db"
conn = sqlite3.connect(database)

data.to_sql("information", conn, if_exists="replace", index=False)

conn.close()

print("Данные успешно внесены в базу данных!")

# Повторное подключение для чтения данных
conn = sqlite3.connect(database)

cursor = conn.cursor()

table_name = "information"
cursor.execute(f"SELECT * FROM {'information'}")
rows = cursor.fetchall()
columns = [description[0] for description in cursor.description]
data = pd.DataFrame(rows, columns=columns)

cursor.close()
conn.close()

data
