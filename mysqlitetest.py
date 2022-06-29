import sqlite3
import pandas as pd
from Commands_For_DataBase import Command
df = pd.read_csv('Processos.csv', sep=';')

# create database
con = sqlite3.connect('Dados.db')

# Cursor
cur = con.cursor()

# Create table
# cur.execute('''CREATE TABLE historico (processo TEXT, link TEXT)''')

# Insere uma linha
# cur.execute("INSERT INTO historico VALUES ('28/06/2022', 'Andamento doido', 1233312333)")

cur.execute('''SELECT * FROM historico;''')

rows = cur.fetchall()
 
for row in rows:
	print(row)
# for i in range(len(df.index)):
#     cur.execute(f"INSERT INTO historico VALUES ('{df['Processos'][i]}', '{df['Links'][i]}')")
    
# #commit the changes to db			
# con.commit()
# #close the connection
# con.close()