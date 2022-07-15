import sqlite3
from FuncsForSPO.sqlite_functions import *

# criando uma conexão persistente "caso feche o programa e abra novamente a base estará criada"
conexao = sqlite3.connect('basededados.db')  # cria a base sem nada, sem tabelas ou registros

# criando um cursor (que é esse cursor que executará os comandos sql na base)
cursor = conexao.cursor()

# cria tabela                                           id inteiro, pk autoincrementada         nome texto   peso float
cursor.execute('''
               CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, peso REAL)
               ''')

# # inserindo registros na tabela criada
# cursor.execute('''
#                INSERT INTO clientes (nome, peso) VALUES ("Gabriel Lopes", 80.5)
#                ''')  # executar os comandos dessa maneira pode ser extremamente inseguro! https://www.devmedia.com.br/sql-injection/6102

# inserindo um registro na tabela criada
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ("Maria", 50))  # dessa maneira já previne o sqlinjection

# #                                                    key dict,  key dict
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {"nome": "João", "peso": 25})  # dessa maneira já previne o sqlinjection

# #                                                    key dict,  key dict
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {"nome": "Floriano", "peso": 113})  # dessa maneira já previne o sqlinjection


### Alterando dados na tabela pelo id
# Atualize o nome para Joana da tabela clientes onde o id é 1
cursor.execute('UPDATE clientes SET nome = ? WHERE id = ?', ('Joana', 1))  ##MUITO COUDADO AO UTILIZAR## 

#### deletando dados da tabela pelo id
# delete da tabela clientes onde o id é 1
# cursor.execute('DELETE FROM clientes WHERE id = ?', (1))

# executa todos os comandos acima
conexao.commit()

#### mostra todos os valores da tabela
# cursor.execute('SELECT * FROM clientes')

### mostra com where SOMENTE QUEM PESA MAIS DE 50
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso', {'peso': 50})

for linha in cursor.fetchall():
    nome, peso = linha # a cada linha vamos ter uma tupla com as colunas
    print(nome)
    print(peso)
    print()

def select_all_from_table(cur, table):
    """SELECT * FROM table

    Exemplo de saída:
        table_collums => id, nome, idade
        
        (1, 'Gabriel', 20)
        (2, 'João', 18)
        (3, 'Riveira', 35)
    
    
    Args:
        cur (Cursor): Cursor do SQLite
        table (Tabela): Tabela do banco de dados
    """
    
    cur.execute(f'SELECT * FROM {table}')
    for i in cursor.fetchall():
        print(i) # print line 
    
    
select_all_from_table(cursor, 'clientes')
    
# vai buscar todos os valores do select para mostrar (é um iterável)
# for linha in cursor.fetchall():
#     identificador, nome, peso = linha # a cada linha vamos ter uma tupla com as colunas
#     print(identificador)
#     print(nome)
#     print(peso)
#     print()













cursor.close()
conexao.close()



"""
161. SQLite: usando o módulo sqlite3

criando base de dados sqlite

nessa aula será tudo pelo python, mas geralmente criamos a base de dados, 
    e depois em outro programa criamos as tabelas, chaves primarias, estrangeiras etc...

# sempre quando temos uma conexao e um cursor, é uma boa prática de programação
    fechar o cursor e a conexao no final do arquivo

as tuplas só funcionam com acima de dois valores cursor.execute('UPDATE clientes SET nome = ? WHERE id = ?', ('Joana', 1))
"""