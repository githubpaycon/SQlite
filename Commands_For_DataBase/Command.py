

def deletar_tabela_sqlite(cur, table_name):
    cur.execute(f'''DROP TABLE {table_name}''')
    
def cria_tabela_3_cols(cursor, table_name, cols: dict, primary_key=True, if_not_exists=True):
    # Cria uma tabela de 3 colunas (passar somente 3 keys)
    # nao precisa mandar a coluna id por padrao ela é id INTEGER PRIMARY KEY
    #  { "COLUNA" : "TIPO DECLARATION AND NOT EXIST..." }
    
    keys = [key for key in cols]  # desempacota dodos as keys do dict
    values = [*cols.values()]  # Desempacota todos os valores do dict
    
    if len(values) == 3 and len(keys) == 3:
        if len(keys) > 3 and primary_key==True:
            raise KeyError(f'Existe mais de 3 colunas -> {cols}')
        
        if primary_key and if_not_exists:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, {keys[0]} {values[0]}, {keys[1]} {values[1]}, {keys[2]} {values[2]})''')
            print('Tabela criada')
        elif if_not_exists:
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} ({keys[0]} {values[0]}, {keys[1]} {values[1]}, {keys[2]} {values[2]})''')
            print('Tabela criada')
        elif not if_not_exists:
            cursor.execute(f'''CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, {keys[0]} {values[0]}, {keys[1]} {values[1]}, {keys[2]} {values[2]})''')
            print('Tabela criada')
        elif not primary_key and not if_not_exists:
            cursor.execute(f'''CREATE TABLE {table_name} ({keys[0]} {values[0]}, {keys[1]} {values[1]}, {keys[2]} {values[2]})''')
            print('Tabela criada')
    else:
        raise KeyError(f'Verifique se as chavers estão iguais, pois só há {len(keys)} chaves')