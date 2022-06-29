def deletar_tabela_sqlite(cur, table_name):
    cur.execute(f'''DROP TABLE {table_name}''')
    
