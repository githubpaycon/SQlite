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


class RoboSEI:
    # limpa o console
    os.system('cls')

    def __init__(self, configs):
        self.configs = configs
        self.__URL = 'https://sei.anatel.gov.br/sei/modulos/pesquisa/md_pesq_processo_pesquisar.php?acao_externa=protocolo_pesquisar&acao_origem_externa=protocolo_pesquisar&id_orgao_acesso_externo=0'
        self.TIMEOUT = self.configs['ROBO_SEI']['tempo_para_esperar']
        self.HEADLESS = self.configs['ROBO_SEI']['headless']
        self.DADOS_BASE = self.le_base()
        self.PATH_TABLE_RESULT = os.path.abspath(r'.\Resultados\Resultado.xlsx')
        self.PATH_TABLE_PERFORMANCE = os.path.abspath(r'.\Resultados\Performance.xlsx')


        # GET RANDOM USER_AGENT
        try:
            ua = UserAgent()
            self.user_agent = ua.random
        except FakeUserAgentError:
            pass

        self.path_cnds = os.path.abspath(r".\CND")
        if os.path.exists(self.path_cnds):
            shutil.rmtree(self.path_cnds)
            os.mkdir(self.path_cnds)
        else:
            os.mkdir(self.path_cnds)

        self.__settings = {
            "recentDestinations": [
                {
                    "id": "Save as PDF",
                    "origin": "local",
                    "account": ""
                }
            ],
            "selectedDestinationId": "Save as PDF",
            "version": 2,
        }

        self.__profile = {
            'printing.print_preview_sticky_settings.appState': json.dumps(self.__settings),
            "savefile.default_directory": f"{self.path_cnds}",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        self.__options = webdriver.ChromeOptions()
        self.__options.add_experimental_option('prefs', self.__profile)
        self.__options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.__options.add_argument('--kiosk-printing')
        self.__options.add_argument("--disable-xss-auditor")
        self.__options.add_argument("--disable-web-security")
        self.__options.add_argument("--allow-running-insecure-content")
        self.__options.add_argument("--disable-extensions")
        self.__options.add_argument("--start-maximized")
        self.__options.add_argument("--no-sandbox")
        self.__options.add_argument("--disable-setuid-sandbox")
        self.__options.add_argument("--disable-webgl")
        self.__options.add_argument("--disable-popup-blocking")
        self.__options.add_argument('--disable-gpu')
        self.__options.add_argument('--incognito')
        self.__options.add_argument('--disable-software-rasterizer')
        self.__options.add_argument('--no-proxy-server')
        self.__options.add_argument("--proxy-server='direct://'")
        self.__options.add_argument('--proxy-bypass-list=*')
        self.__options.add_argument('--disable-dev-shm-usage')
        self.__options.add_argument('disable-infobars')
        self.__options.add_argument(f'user-agent={self.user_agent}')
        if self.HEADLESS == 'True':
            self.__options.add_argument('headless')
        self.__service = Service(ChromeDriverManager().install())
        self.__chrome = Chrome(service=self.__service, options=self.__options)
        self.__wdw = WebDriverWait(self.__chrome, timeout=int(self.TIMEOUT))

        ############ Dados #############
        self.dados_processo = {
            'Processo': [],
            'Tipo': [],
            'Data de Registro': [],
            'Interessados': [],
            'Último Protocolo: Documento / Processo': [],
            'Último Protocolo: Tipo de Documento': [],
            'Último Protocolo: Data do Documento': [],
            'Último Protocolo: Data de Registro': [],
            'Último Protocolo: Unidade': [],
            'Último Andamento: Data & Hora': [],
            'Último Andamento: Unidade': [],
            'Último Andamento: Descrição': [],
            'Link': [],
        }

        self.dados_processo_sheet_anteriores = {
            'Processo': ['NAN'],
            'Tipo': ['NAN'],
            'Data de Registro': ['NAN'],
            'Interessados': ['NAN'],
            'Último Protocolo: Documento / Processo': ['NAN'],
            'Último Protocolo: Tipo de Documento': ['NAN'],
            'Último Protocolo: Data do Documento': ['NAN'],
            'Último Protocolo: Data de Registro': ['NAN'],
            'Último Protocolo: Unidade': ['NAN'],
            'Último Andamento: Data & Hora': ['NAN'],
            'Último Andamento: Unidade': ['NAN'],
            'Último Andamento: Descrição': ['NAN'],
            'Link': ['NAN'],
        }

        ############ Dados #############

    @staticmethod
    def le_base():
        faz_log(f'Lendo arquivo Processos...')
        PATH_BASE = os.path.abspath(r'.\base')

        # Pega todos os arquivos da pasta
        FILES = os.listdir(PATH_BASE)

        # Pega a lista de Arquivos que contem .xlsx e Processos no nome da lista de arquivos
        FILES_XLSX = [PATH_BASE + "\\" + f for f in FILES if ".xlsx" in f and 'Processos' in f]

        if len(FILES_XLSX) > 1:
            faz_log(
                'Existe mais de um arquivo XLSX com o nom PROCESSOS na base. Por favor, feche qualquer planilha aberta em no arquivo Processos.xlsx.\nVerifique se existe de fato mais arquivos com o mesmo nome.\nVeja no log os arquivos...',
                'c')
            faz_log(f'Lista de arquivos: {FILES_XLSX}', 'c')
            fecha_em_x_segundos(5)

        # Tabela Processos
        PROCESSOS_TABLE = pd.read_excel(f'{FILES_XLSX[0]}', sheet_name=0, usecols=['Número de Processos', 'Links'],
                                        dtype=str)

        num_processos = PROCESSOS_TABLE['Número de Processos']
        links = PROCESSOS_TABLE['Links']

        return (num_processos, links)

    def acessa_processos(self):
        qtd_processos = len(self.DADOS_BASE[0].index)
        for i in range(qtd_processos):
            # if i == 5:
            #     self.verifica_com_a_tabela_anterior()
            #     break
            processo = self.DADOS_BASE[0][i]
            link = self.DADOS_BASE[1][i]
            faz_log(f'Recuperando processo {i+1} de {qtd_processos+1}\n'
                    f'Número de Processo {processo}')

            self.__chrome.get(link)
            espera_elemento(self.__wdw, (By.CSS_SELECTOR, '#divInfraAreaTabela'))
            self.recupera_dados_processo(link)
            self.recupera_dados_lista_protocolo()
            self.recupera_dados_lista_andamentos()
        else:
            self.verifica_com_a_tabela_anterior()

    def recupera_dados_processo(self, link):
        n_processo_sei = espera_e_retorna_elemento_text(self.__chrome, self.__wdw,
                                                        (By.CSS_SELECTOR, '#tblCabecalho > tbody > tr~tr>td~td'))
        tipo_sei = espera_e_retorna_elemento_text(self.__chrome, self.__wdw,
                                                  (By.CSS_SELECTOR, '#tblCabecalho > tbody > tr~tr~tr>td~td'))
        data_registro = espera_e_retorna_elemento_text(self.__chrome, self.__wdw,
                                                       (By.CSS_SELECTOR, '#tblCabecalho > tbody > tr~tr~tr~tr>td~td'))
        interessados = espera_e_retorna_elemento_text(self.__chrome, self.__wdw,
                                                      (By.CSS_SELECTOR, '#tblCabecalho > tbody > tr~tr~tr~tr~tr>td~td'))

        if n_processo_sei == ' ' or n_processo_sei == '':
            n_processo_sei = 'NÃO EXISTE'
        if tipo_sei == ' ' or tipo_sei == '':
            tipo_sei = 'NÃO EXISTE'
        if data_registro == ' ' or data_registro == '':
            data_registro = 'NÃO EXISTE'
        if interessados == ' ' or interessados == '':
            interessados = 'NÃO EXISTE'

        self.dados_processo['Processo'].append(n_processo_sei)
        self.dados_processo['Tipo'].append(tipo_sei)
        self.dados_processo['Data de Registro'].append(data_registro)
        self.dados_processo['Interessados'].append(interessados)
        self.dados_processo['Link'].append(link)

    def recupera_dados_lista_protocolo(self):
        doc_processo = espera_e_retorna_elemento_text(self.__chrome, self.__wdw, (
        By.CSS_SELECTOR, '#tblDocumentos > tbody > tr:last-child > td~td > a'))
        tipo_doc = espera_e_retorna_elemento_text(self.__chrome, self.__wdw, (
        By.CSS_SELECTOR, '#tblDocumentos > tbody > tr:last-child > td~td~td'))
        data_doc = espera_e_retorna_elemento_text(self.__chrome, self.__wdw, (
        By.CSS_SELECTOR, '#tblDocumentos > tbody > tr:last-child > td~td~td~td'))
        data_registro = espera_e_retorna_elemento_text(self.__chrome, self.__wdw, (
        By.CSS_SELECTOR, '#tblDocumentos > tbody > tr:last-child > td~td~td~td~td'))
        unidade = espera_e_retorna_elemento_text(self.__chrome, self.__wdw, (
        By.CSS_SELECTOR, '#tblDocumentos > tbody > tr:last-child > td~td~td~td~td~td>a'))

        self.dados_processo['Último Protocolo: Documento / Processo'].append(doc_processo)
        self.dados_processo['Último Protocolo: Tipo de Documento'].append(tipo_doc)
        self.dados_processo['Último Protocolo: Data do Documento'].append(data_doc)
        self.dados_processo['Último Protocolo: Data de Registro'].append(data_registro)
        self.dados_processo['Último Protocolo: Unidade'].append(unidade)

    def recupera_dados_lista_andamentos(self):
        data_hora = espera_e_retorna_elemento_text(self.__chrome, self.__wdw, (
        By.CSS_SELECTOR, '#tblHistorico > tbody > tr:nth-child(2) > td:nth-child(1)'))
        unidade = espera_e_retorna_elemento_text(self.__chrome, self.__wdw, (
        By.CSS_SELECTOR, '#tblHistorico > tbody > tr:nth-child(2) > td:nth-child(2)'))
        descricao = espera_e_retorna_elemento_text(self.__chrome, self.__wdw, (
        By.CSS_SELECTOR, '#tblHistorico > tbody > tr:nth-child(2) > td:nth-child(3)'))

        self.dados_processo['Último Andamento: Data & Hora'].append(data_hora)
        self.dados_processo['Último Andamento: Unidade'].append(unidade)
        self.dados_processo['Último Andamento: Descrição'].append(descricao)

    def verifica_com_a_tabela_anterior(self):
        os.system('cls')

        def joga_os_dados_para_anterior(df_current):
            """Copia, cria um novo df e retorna sem as colunas que mostra que mudou"""
            df = df_current.copy(deep=True)
            df = df.drop(columns=['Andamento: Mudou'])
            df = df.drop(columns=['Protocolo: Mudou'])
            return df

        def reinicia_verificacao(df_atual, df_anterior):
            _qtd_andamentos = len(df_atual['Último Andamento: Data & Hora'])
            for _i in range(_qtd_andamentos):
                if df_anterior['Último Andamento: Data & Hora'][_i] == df_atual['Último Andamento: Data & Hora'][_i]:
                    df_atual['Andamento: Mudou'][_i] = 'Não Mudou'
                else:
                    df_atual['Andamento: Mudou'][_i] = 'Mudou'
                    faz_log('Houve mudança no Andamento!')
                    faz_log('Dados do processo:')
                    faz_log(f'\tNúmero do Processo: {df_atual["Processo"][_i]}')
                    faz_log(f'\tTipo: {df_atual["Tipo"][_i]}')
                    faz_log(f'\tData de Registro: {df_atual["Data de Registro"][_i]}', )
                    faz_log(f'\tInteressados: {df_atual["Interessados"][_i]}')
                    faz_log(f'\tÚltimo Andamento (Execução Atual): {df_atual["Último Andamento: Data & Hora"][_i]}')
                    faz_log(
                        f'\tÚltimo Andamento (Execução Anterior): {df_anterior["Último Andamento: Data & Hora"][_i]}')

                if df_anterior['Último Protocolo: Documento / Processo'][_i] == \
                        df_atual['Último Protocolo: Documento / Processo'][_i]:
                    df_atual['Protocolo: Mudou'][_i] = 'Não Mudou'
                else:
                    df_atual['Protocolo: Mudou'][_i] = 'Mudou'
                    faz_log('Houve mudança no Protocolo!')
                    faz_log('Dados do processo:')
                    faz_log(f'\tNúmero do Processo: {df_atual["Processo"][_i]}')
                    faz_log(f'\tTipo: {df_atual["Tipo"][_i]}')
                    faz_log(f'\tData de Registro: {df_atual["Data de Registro"][_i]}')
                    faz_log(f'\tInteressados: {df_atual["Interessados"][_i]}')
                    faz_log(f'\tÚltimo Protocolo (Execução Atual): {df_atual["Último Protocolo: Documento / Processo"][_i]}')
                    faz_log(f'\tÚltimo Protocolo (Execução Anterior): {df_anterior["Último Protocolo: Documento / Processo"][_i]}')
            else:
                df_anterior = joga_os_dados_para_anterior(df_atual)
                with pd.ExcelWriter(self.PATH_TABLE_RESULT) as writer:
                    df_atual.to_excel(writer, sheet_name='ResultadoAtual', index_label=False, index=False)
                    df_anterior.to_excel(writer, sheet_name='ResultadoAnterior', index_label=False, index=False)
        # pega os dataframes
        df_atual = pd.DataFrame(self.dados_processo)  # pega dataframe da pesquisa atual
        try:
            df_anterior = pd.read_excel(self.PATH_TABLE_RESULT, sheet_name='ResultadoAnterior', dtype=str)  # Pega dataframe via file
        except ValueError:
            df_anterior = df_atual

        # Cria colunas para manter as tabelas iguais
        df_atual['Andamento: Mudou'] = 'NaN'
        df_atual['Protocolo: Mudou'] = 'NaN'

        df_anterior['Andamento: Mudou'] = 'NaN'
        df_anterior['Protocolo: Mudou'] = 'NaN'

        qtd_andamentos = len(df_atual['Último Andamento: Data & Hora'])
        try:
            for i in range(qtd_andamentos):
                if df_anterior['Último Andamento: Data & Hora'][i] == df_atual['Último Andamento: Data & Hora'][i]:
                    df_atual['Andamento: Mudou'][i] = 'Não Mudou'
                else:
                    df_atual['Andamento: Mudou'][i] = 'Mudou'
                    faz_log('Houve mudança no Andamento!')
                    faz_log('Dados do processo:')
                    faz_log(f'\tNúmero do Processo: {df_atual["Processo"][i]}')
                    faz_log(f'\tTipo: {df_atual["Tipo"][i]}')
                    faz_log(f'\tData de Registro: {df_atual["Data de Registro"][i]}', )
                    faz_log(f'\tInteressados: {df_atual["Interessados"][i]}')
                    faz_log(f'\tÚltimo Andamento (Execução Atual): {df_atual["Último Andamento: Data & Hora"][i]}')
                    faz_log(
                        f'\tÚltimo Andamento (Execução Anterior): {df_anterior["Último Andamento: Data & Hora"][i]}')

                if df_anterior['Último Protocolo: Documento / Processo'][i] == df_atual['Último Protocolo: Documento / Processo'][i]:
                    df_atual['Protocolo: Mudou'][i] = 'Não Mudou'
                else:
                    df_atual['Protocolo: Mudou'][i] = 'Mudou'
                    faz_log('Houve mudança no Protocolo!')
                    faz_log('Dados do processo:')
                    faz_log(f'\tNúmero do Processo: {df_atual["Processo"][i]}')
                    faz_log(f'\tTipo: {df_atual["Tipo"][i]}')
                    faz_log(f'\tData de Registro: {df_atual["Data de Registro"][i]}')
                    faz_log(f'\tInteressados: {df_atual["Interessados"][i]}')
                    faz_log(
                        f'\tÚltimo Protocolo (Execução Atual): {df_atual["Último Protocolo: Documento / Processo"][i]}')
                    faz_log(
                        f'\tÚltimo Protocolo (Execução Anterior): {df_anterior["Último Protocolo: Documento / Processo"][i]}')
            else:
                df_anterior = joga_os_dados_para_anterior(df_atual)
                with pd.ExcelWriter(self.PATH_TABLE_RESULT) as writer:
                    df_atual.to_excel(writer, sheet_name='ResultadoAtual', index_label=False, index=False)
                    df_anterior.to_excel(writer, sheet_name='ResultadoAnterior', index_label=False, index=False)
        except KeyError:
            faz_log('Existe um processo a mais ou a menos na tabela, rode o robô novamente e não apague nada na tabela Resultado.xlsx')
            df_anterior = joga_os_dados_para_anterior(df_atual)
            with pd.ExcelWriter(self.PATH_TABLE_RESULT) as writer:
                df_atual.to_excel(writer, sheet_name='ResultadoAtual', index_label=False, index=False)
                df_anterior.to_excel(writer, sheet_name='ResultadoAnterior', index_label=False, index=False)
            reinicia_verificacao(df_atual, df_anterior)

    def faz_tabela_performance(self, data, inicio, fim, total):
        try:
            df_performance = pd.read_excel(self.PATH_TABLE_PERFORMANCE, sheet_name='Performance', dtype=str)  # Pega dataframe via file
        except FileNotFoundError:
            df_performance = pd.DataFrame({
                'Data Início': [f'O robô iniciou no dia {str(data)}'],
                'Hora Início': [f'O robô iniciou em {str(inicio)}'],
                'Hora Fim': [f'O robô finalizou em {str(fim)}'],
                'Tempo Total': [f'{str(total)} minuto(s)'],
            })

            df_performance.to_excel(self.PATH_TABLE_PERFORMANCE, 'Performance', index=False, encoding='utf-8')
            quit()

        df_append = pd.DataFrame({
            'Data Início': [f'O robô iniciou no dia {str(data)}'],
            'Hora Início': [f'O robô iniciou em {str(inicio)}'],
            'Hora Fim': [f'O robô finalizou em {str(fim)}'],
            'Tempo Total': [f'{str(total)} minuto(s)'],
            })

        df_new = df_performance.append(df_append, ignore_index=True)

        df_new.to_excel(self.PATH_TABLE_PERFORMANCE, 'Performance', index=False, encoding='utf-8')



