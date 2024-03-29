from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from time import sleep

def url_atual(driver):
    """
    ### Função RETORNA a url atual

    Args:
        driver (WebDriver): Seu Webdriver (Chrome, Firefox, Opera...)

    Returns:
        (str): URL atual da janela atual
    """
    return driver.current_url

def atualiza_page_atual(driver):
    """
    ### Função atualiza a página atual da janela atual

    Args:
        driver (WebDriver): Seu Webdriver (Chrome, Firefox, Opera...)
        
    """
    driver.refresh()
        
        
def espera_e_clica_em_varios_elementos(driver, wdw, locator: tuple):
    
    wdw.until(EC.presence_of_all_elements_located(locator))
    elements = driver.find_elements(*locator)
    len_elements = len(elements)

    for i in range(len_elements):
        elements[i].click()
        
        
def espera_elemento_disponivel_e_clica(driver, wdw, locator: tuple):
    """
    ### Função que espera pelo elemento enviado do locator e clica nele assim que possível

    Args:
        driver (WebDriver): Seu Webdriver (Chrome, Firefox, Opera)
        wdw (WebDriverWait): Seu WebDriverWait
        locator (tuple): A localização do elemento no DOM (By.CSS_SELECTOR, '#IdButton')
        
    """
    wdw.until(EC.element_to_be_clickable(locator)).click()
    # driver.find_element(*locator).click()


def espera_elemento(wdw, locator: tuple):
    """
    ### Função que espera pelo elemento enviado do locator

    Args:
        wdw (WebDriverWait): Seu WebDriverWait
        locator (tuple): A localização do elemento no DOM (By.CSS_SELECTOR, '#IdButton')
        
    """
    return wdw.until(EC.element_to_be_clickable(locator))

def espera_2_elementos(wdw, locator1: tuple, locator2 : tuple):
    """
    ### Função que espera pelo elemento enviado do locator

    Args:
        wdw (WebDriverWait): Seu WebDriverWait
        locator (tuple): A localização do elemento no DOM (By.CSS_SELECTOR, '#IdButton')
        
    """
    try:
        wdw.until(EC.element_to_be_clickable(locator1))
    except Exception:
        wdw.until(EC.element_to_be_clickable(locator2))
        


def espera_elemento_e_envia_send_keys(driver, wdw, string, locator: tuple):
    """
    ### Função que espera pelo elemento enviado do locator e envia o send_keys no input ou textarea assim que possível

    Args:
        driver (WebDriver): Seu Webdriver (Chrome, Firefox, Opera)
        wdw (WebDriverWait): Seu WebDriverWait
        locator (tuple): A localização do elemento no DOM (By.CSS_SELECTOR, '#IdButton')
        
    """
    wdw.until(EC.element_to_be_clickable(locator))
    try:
        driver.find_element(*locator).send_keys(string)
    except StaleElementReferenceException:
        wdw.until(EC.element_to_be_clickable(locator))
        driver.find_element(*locator).send_keys(string)
    
    
def espera_e_retorna_lista_de_elementos(driver, wdw, locator: tuple):
    """
    ### Função espera e retorna uma lista de elementos indicados no locator

    Args:
        driver (Webdriver): Seu Webdriver (Chrome, Opera, Firefox)
        wdw (WebDriverWait): Seu WebDriverWait
        locator (tuple): A tupla indicando a localização do elemento no DOM ("BY_SELECTOR", "#list_arms").

    Returns:
        list: Lista com os elementos com o formato de Objetos (lista de Objetos)
    """
    wdw.until(EC.element_to_be_clickable(locator))
    return driver.find_elements(*locator)


def espera_e_retorna_lista_de_elementos_text_from_id(driver, wdw, locator: tuple):
    """
    ### Função espera e retorna uma lista de elementos com id
    

    Args:
        driver (WebDriver): Seu Webdriver (Chrome, Firefox, Opera)
        wdw (WebDriverWait): Seu WebDriverWait
        locator (tuple): A tupla indicando a localização do elemento no DOM ("BY_SELECTOR", "#list_arms").

    Returns:
        list: Lista de textos dos elementos com id -> [adv 1, adv 2, adv 3, adv 4, adv 5]
    """
    wdw.until(EC.element_to_be_clickable(locator))
    webelements = driver.find_elements(*locator)
    id = 1
    elementos_com_id = []
    for element in webelements:
        if element.text == ' ':
            elementos_com_id.append(element.text)
        else:
            elementos_com_id.append(f'{element.text} {id}')
        id += 1
    else:
        return elementos_com_id
    
# utilizado para o STJ   
# def espera_e_retorna_lista_de_elementos_text_from_id_esse_tribunal(driver, wdw, locator: tuple=("BY_SELECTOR", "WEBELEMENT")):
#     """Função espera e retorna 

#     Args:
#         driver (_type_): _description_
#         wdw (_type_): _description_
#         locator (tuple, optional): _description_. Defaults to ("BY_SELECTOR", "WEBELEMENT").

#     Returns:
#         _type_: _description_
#     """
#     if locator == ("BY_SELECTOR", "WEBELEMENT"):
#         print('Adicione um locator!!!!')
#         return
#     wdw.until(EC.element_to_be_clickable(locator))
#     webelements = driver.find_elements(*locator)
#     id = 1
#     elementos_com_id = []
#     for element in webelements:
#         if element.text == ' ':
#             elementos_com_id.append(f'VOLUME(S) col{id}')
#         else:
#             elementos_com_id.append(f'{element.text} col{id}')
#         id += 1
#     else:
#         return elementos_com_id


def espera_e_retorna_lista_de_elementos_text(driver, wdw, locator: tuple):
    """
    ### Função espera e retorna uma lista com os textos dos elementos

    Args:
        driver (Webdriver): Seu Webdriver (Chrome, Firefox, Opera)
        wdw (WebDriverWait): Seu WebDriverWait
        locator (tuple): A tupla indicando a localização do elemento no DOM ("BY_SELECTOR", "#list_arms").

    Returns:
        list: Lista dos textos dos elementos
    """
    wdw.until(EC.element_to_be_clickable(locator))
    return [element.text for element in driver.find_elements(*locator)]



def espera_e_retorna_conteudo_do_atributo_do_elemento_text(driver, wdw, atributo, locator: tuple):
    """
    ### Função que espera pelo elemento e retorna o texto do atributo do elemento escolhido

    Args:
        driver (Webdriver): Seu Webdriver (Chrome, Firefox)
        wdw (WebDriverWait): Seu WebDriverWait
        atributo (str): O atributo que deseja recuperar, como um href, id, class, entre outros
        locator (tuple): A localização do elemento no DOM ("By.CSS_SELECTOR", "body > div > a").

    Returns:
        str: retorna uma string com o valor do atributo do elemento
    """
    wdw.until(EC.element_to_be_clickable(locator))
    return driver.find_element(*locator).get_attribute(atributo)


def espera_e_retorna_conteudo_dos_atributos_dos_elementos_text(driver, wdw, atributo, locator: tuple=("BY_SELECTOR", "WEBELEMENT")):
    """
    ### Função espera e retorna o valor dos atributos de vários elementos

    Args:
        driver (Webdriver): Seu Webdriver (Chrome, Firefox)
        wdw (WebDriverWait): Seu WebDriverWait
        atributo (str): Atributo (esse deve existir em todos os elementos)
        locator (tuple): Posição dos elementos no DOM.("By.CSS_SELECTOR", "#list_works").

    Returns:
        list: Lista com os atributos de todos os elementos (é necessário que o atibuto enviado exista em todos os elementos como um href)
    """
    if locator == ("BY_SELECTOR", "WEBELEMENT"):
        print('Adicione um locator!!!!')
        return
    wdw.until(EC.element_to_be_clickable(locator))
    atributos = driver.find_elements(*locator)
    elementos_atributos = [atributo_selen.get_attribute(atributo) for atributo_selen in atributos]
    return elementos_atributos
        
        
def espera_e_retorna_elemento_text(driver,  wdw, locator: tuple):
    """Função espera o elemento e retorna o seu texto

    Args:
        driver (Webdriver): Webdriver (Chrome, Firefox)
        wdw (WebDriverWait): WebDriverWait
        locator (tuple): Localização do elemento no DOM. ("By.CSS_SELECTOR", "#name")

    Returns:
        str: Retorna a string de um elemento
    """
    wdw.until(EC.element_to_be_clickable(locator))
    return driver.find_element(*locator).text
    
    
def vai_para_a_primeira_janela(driver):
    """Vai para a primeira janela, geralmente a primeira que é iniciada

    Args:
        driver (_type_): WebDriver
    """
    window_ids = driver.window_handles # ids de todas as janelas
    driver.switch_to.window(window_ids[0])
    
    
def espera_abrir_n_de_janelas_e_muda_para_a_ultima_janela(driver, wdw, num_de_janelas: int=2):
    """Função espera abrir o numero de janelas enviada por ti, e quando percebe que abriu, muda para a última janela aberta

    Args:
        driver (Webdriver): Webdriver (Chrome, Firefox)
        wdw (WebDriverWait): WebDriver
        num_de_janelas (int): Quantidade de janelas esperadas para abrie. O padrão é 2.
    """
    print(f'Você está na janela -> {driver.current_window_handle}')
    wdw.until(EC.number_of_windows_to_be(num_de_janelas))
    print(f'Agora, você tem {len(driver.window_handles)} janelas abertas')
    todas_as_windows = driver.window_handles
    driver.switch_to.window(todas_as_windows[-1])
    print(f'Agora, você está na janela -> {driver.current_window_handle}')
    
    
def procura_pela_janela_que_contenha_no_titulo(driver, title_contain_switch : str): # quero que pelo menos um pedaco do titulo que seja str
    """
    ### Essa função muda de janela quando o título tiver pelo menos algo igual ao parametro enviado
    #### Ex -> Minha janela = janela
    
    Args:
        driver (Webdriver): Webdriver (Chrome, Firefox)
        title_contain_switch (str) : Pelo menos um pedaco do titulo exista para mudar para a página 
    """
    window_ids = driver.window_handles # ids de todas as janelas

    for window in window_ids:
        driver.switch_to_window(window)  
        if title_contain_switch in driver.title:
            break
    else:
        print(f'Janela não encontrada!\n'
            f'Verifique o valor enviado {title_contain_switch}')
    
    
def fecha_janela_atual(driver):
    """
    ### Função que fecha a janela atual

    Args:
        driver (WebDriver): Seu WebDriver (Chrome, Firefox)
    """
    driver.close()


def espera_enquanto_nao_tem_resposta_do_site(driver, wdw, locator : tuple):
    """
    ### Função que espera enquanto o site não tem resposta
    
    #### ESSA FUNÇÃO SÓ DEVE SER USADA CASO VOCÊ TENHA CERTEZA QUE O SITE POSSA VIR A CAIR

    Args:
        driver (WebDriver): Seu WebDriver (Chrome, Firefox)
        wdw (WebDriverWait): WebDriverWait
        locator (tuple): Localização do elemento no DOM. ("By.CSS_SELECTOR", "#ElementQueSempreEstaPresente")
    """
    try:
        element = wdw.until(EC.element_to_be_clickable(locator))
        if element:
            return element
    except TimeoutException:
        print('Talvez a página tenha dado algum erro, vou atualiza-lá')
        sleep(2)
        try:
            driver.refresh()
            element = wdw.until(EC.element_to_be_clickable(locator))
            if element:
                print('Voltou!')
                return element
        except TimeoutException:
            print('A página ainda não voltou, vou atualiza-lá')
            sleep(2)
            try:
                driver.refresh()
                element = wdw.until(EC.element_to_be_clickable(locator))
                if element:
                    print('Voltou!')
                    return element
            except TimeoutException:
                print('Poxa, essa será a última vez que vou atualizar a página...')
                sleep(2)
                try:
                    driver.refresh()
                    element = wdw.until(EC.element_to_be_clickable(locator))
                    if element:
                        print('Voltou!')
                        return element
                except TimeoutException:
                    print("Olha, não foi possível. A página provavelmente caiu feio :(")
                    print("Infelizmente o programa vai ser finalizado...")
                    driver.quit()
                   
                   
def volta_paginas(driver, qtd_pages_para_voltar : int=1, espera_ao_mudar=0):
    """
    ### Essa função volta (back) quantas páginas você desejar

    Args:
        driver (_type_): Seu webdriver
        qtd_pages_para_voltar (int): Quantidade de páginas que serão voltadas. O padrão é uma página (1).
        espera_ao_mudar (int or float, optional): Se você quer esperar um tempo para voltar uma página. O padrão é 0.
        
    Uso:
        volta_paginas(driver=self.chrome, qtd_pages_para_voltar=3, espera_ao_mudar=1)
    """
    if espera_ao_mudar == 0:
        for back in range(qtd_pages_para_voltar):
            driver.back()
    else:
        for back in range(qtd_pages_para_voltar):
            sleep(espera_ao_mudar)
            driver.back()
    
    
# Em desenvolvimento (ESTUDOS)
    
# def muda_p_alerta_e_clica_em_accept(driver, wdw, sleeping):
    # sleep(sleeping)
    # alerta = driver.switch_to.alert
    # alerta.accept()


# def muda_p_alerta_e_clica_em_dismiss(self):
    # alerta = self.chrome.switch_to.alert
    # alerta.dismiss()
    
    
# def espera_input_e_limpa(driver, wdw, locator : tuple):
    # wdw.until(EC.element_to_be_clickable(locator))
    # driver.find_element(*locator).clear
    
# Em desenvolvimento (ESTUDOS)

def espera_input_limpa_e_envia_send_keys_preessiona_esc(driver, wdw, keys : str, locator : tuple):
    from selenium.common.exceptions import StaleElementReferenceException
    from selenium.webdriver.common.keys import Keys

    """
    ### Função espera pelo input ou textarea indicado pelo locator, limpa ele e envia os dados

    Args:
        driver (_type_): Seu webdriver
        wdw (_type_): WebDriverWait criado em seu código
        keys (str): Sua string para enviar no input ou textarea
        locator (tuple): Tupla que contém a forma e o caminho do elemento (By.CSS_SELECTOR, '#myelementid')
    """
    try:
        wdw.until(EC.element_to_be_clickable(locator))
        driver.find_element(*locator).click()
        driver.find_element(*locator).send_keys(Keys.ESCAPE)
        driver.find_element(*locator).clear()
        driver.find_element(*locator).send_keys(keys)
    except StaleElementReferenceException:
        wdw.until(EC.element_to_be_clickable(locator))
        driver.find_element(*locator).click()
        driver.find_element(*locator).send_keys(Keys.ESCAPE)
        driver.find_element(*locator).clear()
        driver.find_element(*locator).send_keys(keys)
    
def espera_input_limpa_e_envia_send_keys(driver, wdw, keys : str, locator : tuple):
    from selenium.common.exceptions import StaleElementReferenceException
    """
    ### Função espera pelo input ou textarea indicado pelo locator, limpa ele e envia os dados

    Args:
        driver (_type_): Seu webdriver
        wdw (_type_): WebDriverWait criado em seu código
        keys (str): Sua string para enviar no input ou textarea
        locator (tuple): Tupla que contém a forma e o caminho do elemento (By.CSS_SELECTOR, '#myelementid')
    """
    try:
        wdw.until(EC.element_to_be_clickable(locator))
        driver.find_element(*locator).click()
        driver.find_element(*locator).clear()
        driver.find_element(*locator).send_keys(keys)
    except StaleElementReferenceException:
        wdw.until(EC.element_to_be_clickable(locator))
        driver.find_element(*locator).click()
        driver.find_element(*locator).clear()
        driver.find_element(*locator).send_keys(keys)
    
    
    
def espera_elemento_sair_do_dom(wdw, locator):
    return wdw.until_not(EC.presence_of_element_located(locator))
    
    
def pega_somente_numeros_de_uma_str(string):
    """
    ### Função que retorna uma LISTA somente com os números de uma string
    #### Removida do site: https://www.delftstack.com/pt/howto/python/python-extract-number-from-string/#:~:text=Utilizar%20a%20Compreens%C3%A3o%20da%20Lista,%C3%A9%20encontrado%20atrav%C3%A9s%20da%20itera%C3%A7%C3%A3o.
       
    Args:
        string (str): String que tem números com letras
    """
    numbers = [int(temp) for temp in string.split() if temp.isdigit()]
    print(f'A string tem {len(numbers)}, {numbers}')
    return numbers
    
    
def espera_elemento_ficar_ativo_e_clica(driver, wdw, locator : tuple):

    wdw.until_not(EC.element_to_be_selected(driver.find_element(*locator)))
            # qualquer h1 que aparecer vai falar (apareceu)

    print('O Botão está ativo')

    driver.find_element(*locator).click()
    
    
def clica_no_elemento_x_vezes_se_interceptado(driver, wdw, locator : tuple):
    from selenium.common.exceptions import ElementClickInterceptedException
    
    wdw.until_not(EC.element_to_be_clickable(driver.find_element(*locator)))

    try:
        driver.find_element(*locator).click()
    except ElementClickInterceptedException:
        sleep(1)
        driver.find_element(*locator).click()
    
    
    
def espera_elemento_nao_estar_mais_visivel(wdw, locator):
    return wdw.until_not(EC.visibility_of(*locator))
    
    

def find_window_to_title_contain(driver, title_contain_switch: str): # quero que pelo menos um pedaco do titulo que seja str
    """
    ### Essa função muda de janela quando o título tiver pelo menos algo igual ao parametro enviado
    #### Ex -> Minha janela = janela
    
    para cada janela em ids das janelas
    muda para a janela
    se a janela for ao menos de um pedaço do titulo que passei
        em title_contain_switch
    para de executar
    """
    window_ids = driver.window_handles # ids de todas as janelas

    for window in window_ids:
        driver.switch_to_window(window)  
        if title_contain_switch in driver.title:
            break
    else:
        print(f'Janela não encontrada!\n'
              f'Verifique o valor enviado {title_contain_switch}')
    
    
def find_window_to_url(driver, url_switch: str): # quero uma url que seja str
    """
    ### Essa função muda de janela quando a url for igual ao parametro enviado
    #### Ex -> https://google.com.br  = https://google.com.br
    
    para cada janela em ids das janelas
    muda para a janela
    se a janela for do titulo que passei
        em title_switch
    para de executar
    """
    window_ids = driver.window_handles # ids de todas as janelas

    for window in window_ids:
        driver.switch_to_window(window)
        if driver.current_url == url_switch:
            break
        else:
            print(f'Janela não encontrada!\n'
                f'Verifique o valor enviado "{url_switch}"')
          
def find_window_to_url_contain(driver, contain_url_switch: str): # quero uma url que seja str
    """
    ### Essa função muda de janela quando a url conter no parametro enviado
    #### Ex -> https://google.com.br  = google
    
    para cada janela em ids das janelas
    muda para a janela
    se a janela for do titulo que passei
        em title_switch
    para de executar
    """
    window_ids = driver.window_handles # ids de todas as janelas

    for window in window_ids:
        driver.switch_to.window(window)
        if contain_url_switch in driver.current_url:
            break
        else:
            print(f'Janela não encontrada!\n'
                f'Verifique o valor enviado "{contain_url_switch}"')
        
        
# def avisa_quando_fecha_janela(wdw, num_de_janelas: int=2):
#     qtd_janelas = wdw.until(EC.number_of_windows_to_be(num_de_janelas))
    
#     if qtd_janelas == num_de_janelas:
#         if wdw.until(EC.new_window_is_opened(2))
    
#     tentativas = 10
    
#     while tentativas != 0:
#         sleep(1)
#         if qtd_janelas == num_de_janelas:
#             while qtd_janelas == num_de_janelas:
#                 qtd_janelas = wdw.until(EC.number_of_windows_to_be(num_de_janelas))
#             else:
#                 return True
#         else:
#             tentativas -= 1
#             continue
#     else:
#         print('NAO ACHOU JANELAS')
        
        
def verifica_se_diminuiu_qtd_de_janelas(driver, qtd_de_w):
    if len(driver.window_handles) == qtd_de_w:
        while len(driver.window_handles) >= qtd_de_w:
            ...
        else:
            window_ids = driver.window_handles # ids de todas as janelas
            driver.switch_to.window(window_ids[1])  # vai para a ultima window
            driver.close()
    else:
        verifica_se_diminuiu_qtd_de_janelas(driver, qtd_de_w)
        
        
        
        
        
def find_window_to_url_contain_and_close_window(driver, contain_url_to_switch: str): # quero uma url que seja str
    """
    ### Essa função muda de janela quando a url conter no parametro enviado
    #### Ex -> https://google.com.br  = google
    
    para cada janela em ids das janelas
    muda para a janela
    se a janela for do titulo que passei
        em title_switch
    para de executar
    """
    window_ids = driver.window_handles # ids de todas as janelas

    for window in window_ids:
        driver.switch_to.window(window)
        if contain_url_to_switch in driver.current_url:
            driver.close()
            break
        

    
    
    
    
###########################################################
######### Padrão de classe __init__ para projetos #########
###########################################################

"""
from functions_selenium import *
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import (EXEÇÕES DO SELENIUM PARA TRATAR)
from time import sleep
import os

class Robo:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    def __init__(self, url='https://www.google.com', headless=0):
        
        if headless:
            self.__s = Service(ChromeDriverManager().install())
            self.__options = ChromeOptions()
            self.__options.add_argument("--headless")
            self.__options.add_experimental_option("excludeSwitches", ["enable-logging"])
            self.__chrome = Chrome(service=self.__s, chrome_options=self.__options)
            self.__chrome.maximize_window()
            self.__chrome.get(url)
            self.__wdw = WebDriverWait(driver=self.__chrome, timeout=10, poll_frequency=0.5)
        else:
            self.__s = Service(ChromeDriverManager().install())
            self.__options = ChromeOptions()
            self.__options.add_experimental_option("excludeSwitches", ["enable-logging"])
            self.__chrome = Chrome(service=self.__s, chrome_options=self.__options)
            self.__chrome.maximize_window()
            self.__chrome.get(url)
            self.__wdw = WebDriverWait(driver=self.__chrome, timeout=10, poll_frequency=0.5)
"""

###########################################################
######### Padrão de classe __init__ para projetos #########
##########################################################







####################################################################
######### Padrão de classe __init__ para projetos COM ELAW #########
####################################################################
"""
from datetime import datetime
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import pandas as pd
import os

class RoboComElaw:
    # limpa o console
    os.system('cls')
    def __init__(self, headless : bool):
        self.__url = 'https://carrefour.elaw.com.br/'
        self.__options = webdriver.ChromeOptions()
        self.__options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.__options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.__options.add_argument("--disable-xss-auditor")
        self.__options.add_argument("--disable-web-security")
        self.__options.add_argument("--allow-running-insecure-content")
        self.__options.add_argument("--disable-extensions")
        self.__options.add_argument("--start-maximized")
        self.__options.add_argument("--no-sandbox")
        self.__options.add_argument("--disable-setuid-sandbox")
        self.__options.add_argument("--disable-webgl")
        self.__options.add_argument("--disable-popup-blocking")
        if headless:
            self.__options.add_argument('--headless')
            self.__options.add_argument('--disable-gpu')
            self.__options.add_argument('--disable-software-rasterizer')
            self.__options.add_argument('--no-proxy-server')
            self.__options.add_argument("--proxy-server='direct://'")
            self.__options.add_argument('--proxy-bypass-list=*')
            self.__options.add_argument('--disable-dev-shm-usage')
        self.__service = Service(ChromeDriverManager(log_level=False, print_first_line=False).install())
        self.__chrome = Chrome(service=self.__service, options=self.__options)
        self.__chrome.get(self.__url)
        self.__wdw = WebDriverWait(self.__chrome, timeout=20)
"""


####################################################################
######### Padrão de classe __init__ para projetos COM ELAW #########
####################################################################