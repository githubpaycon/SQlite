import sqlite3
from h11 import Data
import pandas as pd
from Commands_For_DataBase import Command

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from src.tools.functions.functions_for_py import *
from src.tools.functions.functions_selenium import *
from src.tools.log.log_manager import faz_log
from src.tools.config.config_parser import ConfigParserClaro
from src.tools.ui.windows import Windows
import json
import pandas as pd
import os
from datetime import datetime
from fake_useragent import UserAgent
from fake_useragent import FakeUserAgentError


# create database
con = sqlite3.connect('Dados.db')

# Cursor
cur = con.cursor()

cols = {'c1': 'TEXT',
        'c2': 'text',
        'c2': 'integer'}

Command.cria_tabela_3_cols(cur, 'batata', cols=cols)

# # Create table
# cur.execute('''CREATE TABLE IF NOT EXISTS mercadolivre (id_produto INTEGER PRIMARY KEY, produto TEXT, descricao_produto TEXT, preco_produto TEXT)''')

# # Insere uma linha
# # cur.execute("INSERT INTO historico VALUES ('28/06/2022', 'Andamento doido', 1233312333)")
# # for i in range(len(self.resultados)):

# for i in range(len(nome_do_produto)):
#     cur.execute("""INSERT OR REPLACE INTO mercadolivre(id_produto, produto, descricao_produto, preco_produto) VALUES (?,?,?,?);""", (i, self.preco_do_produto[i], self.nome_do_produto[i], self.descricao_produto[i]))

# cur.execute('''SELECT * FROM mercadolivre;''')

# rows = cur.fetchall()

# for row in rows:
#     print(row)
    
# #commit the changes to db			
# con.commit()
# #close the connection
# con.close()