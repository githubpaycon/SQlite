from Commands_For_DataBase import Command
import sqlite3

con = sqlite3.connect('Dados.db')

# Cursor
cur = con.cursor()

Command.deletar_tabela_sqlite(cur, 'processos')