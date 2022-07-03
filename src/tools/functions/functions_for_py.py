from datetime import datetime
from time import sleep
import os, sys, psutil, shutil, platform

from src.tools.log.log_manager import faz_log
def data_atual():
    """Função retorna a data atual no formato dd/mm/yyyy"""
    e = datetime.now()
    return f'{e.day}/{e.month}/{e.year}'

def times():
    """Função retorna o tempo do dia, por exemplo, Bom dia, Boa tarde e Boa noite

    Returns:
        str: Periodo do dia, por exemplo, Bom dia, Boa tarde e Boa noite
    """
    import datetime
    hora_atual = datetime.datetime.now()
    if hora_atual.hour < 12:
        return 'Bom dia!'
    elif 12 <= hora_atual.hour < 18:
        return 'Boa tarde!'
    else:
        return 'Boa noite!'



def psutil_verifica(nome_do_exe : str):
    # pip install psutil
    """Função verifica se executavel está ativo ou não

    Args:
        nome_do_exe (str): Nome do executavel -> notepad.exe, chrome.exe
    """
    exe = nome_do_exe in (i.name() for i in psutil.process_iter())

    while exe:
        exe = nome_do_exe in (i.name() for i in psutil.process_iter())
        return exe
    else:
        return exe

def verifica_se_caminho_existe(path_file_or_dir: str):
    if os.path.exists(path_file_or_dir):
        return True
    else:
        return False


def deixa_arquivos_ocultos_ou_n(path_file_or_dir : str, oculto : bool=True):
    import ctypes
    from stat import FILE_ATTRIBUTE_ARCHIVE
    FILE_ATTRIBUTE_HIDDEN = 0x02

    if oculto:
        ctypes.windll.kernel32.SetFileAttributesW(path_file_or_dir, FILE_ATTRIBUTE_HIDDEN)
    else:
        ctypes.windll.kernel32.SetFileAttributesW(path_file_or_dir, FILE_ATTRIBUTE_ARCHIVE)
        
    # HIDDEN = OCULTO
    # ARCHIVE = Ñ OCULTO


def fazer_requirements_txt():
    os.system("pip freeze > requirements.txt")
    
    
def limpa_terminal_e_cmd():
    """Essa função limpa o Terminal / CMD no Linux e no Windows"""
    
    os.system('cls' if os.name == 'nt' else 'clear')

def print_bonito(string : str, efeito='=', quebra_ultima_linha : bool=True):
    """Faz um print com separadores
    

    Args:
        string (str): o que será mostrado
        
    
    Exemplo:
        print_bonito('Bem vindo')
    
            =============
            = Bem vindo =
            =============
    
    
    """
    try:
        if len(efeito) != 1:
            print('O EFEITO DEVE SER SOMENTE UMA STRING efeito="="\n'
                '=========\n'
                '== Bem ==\n'
                '=========\n')
            return
        else:
            ...
        
        if quebra_ultima_linha:
            print(efeito*2 + efeito*len(string) + efeito*4)
            print(efeito*2 + ' '+string+' ' + efeito*2)
            print(efeito*2 + efeito*len(string) + efeito*4)
            print('')
        else:
            print(efeito*2 + efeito*len(string) + efeito*4)
            print(efeito*2 + ' '+string+' ' + efeito*2)
            print(efeito*2 + efeito*len(string) + efeito*4)
    except TypeError:
        print('O tipo de string, tem que ser obviamente, string | texto')
    
def instalar_bibliotecas_globalmente():
    """
        Instalar bibliotecas
            * pandas
            * unidecode
            * openpyxl
            * pyinstaller==4.6
            * selenium
            * auto-py-to-exe.exe
            * webdriver-manager
            * xlsxwriter
    """
    print('Instalando essas bibliotecas:\n'
          ' *pandas\n'
          ' *unidecode\n'
          ' *openpyxl\n'
          ' *pyinstaller==4.6\n'
          ' *selenium\n'
          ' *auto-py-to-exe.exe\n'
          ' *webdriver-manager\n'
          ' *xlsxwriter\n')
    aceita = input('você quer essas bibliotecas mesmo?s/n\n >>> ')
    if aceita == 's':
        os.system("pip install pandas unidecode openpyxl pyinstaller==4.6 selenium auto-py-to-exe webdriver-manager xlsxwriter")
        print('\nPronto')
    if aceita == '':
        os.system("pip install pandas unidecode openpyxl pyinstaller==4.6 selenium auto-py-to-exe webdriver-manager xlsxwriter")
        print('\nPronto')
    if aceita == 'n':
        dependencias = input('Escreva as dependencias separadas por espaço\nEX: pandas selenium pyautogui\n>>> ')
        os.system(f'pip install {dependencias}')
        print('\nPronto')
        sleep(3)
    
def criar_ambiente_virtual():
    nome_da_env = input('')
    os.system(f'python -m venv {nome_da_env}')
    print(f'Ambiente Virtual com o nome {nome_da_env} foi criado com sucesso!')
    sleep(2)
    
def restart_program():
    os.execl(sys.executable, sys.executable, *sys.argv)
    
def print_colorido(string : str, color='default', bolder : bool=False):
    """Dê um print com saida do terminal colorida

    Args:
        string (str): string que você quer colorir na saida do terminal / cmd
        color (str, optional): cor que você deseja colorir a string. Defaults to 'default'.
        bolder (bool, optional): se você deseja deixar a string com negrito / bolder. Defaults to False.
        
    Color List:
        white;
        red;
        green;
        blue;
        cyan;
        magenta;
        yellow;
        black.
    """
    color.lower()
    
    win_version = platform.system()+' '+platform.release()
    
    if 'Windows 10' in win_version:
        if bolder == False:
            if color == 'default':  # white
                print(string)
            elif color == 'red':  # red
                print(f'\033[31m{string}\033[m')
            elif color == 'green':  # green
                print(f'\033[32m{string}\033[m')
            elif color == 'blue':  # blue
                print(f'\033[34m{string}\033[m')
            elif color == 'cyan':  # cyan
                print(f'\033[36m{string}\033[m')
            elif color == 'magenta':  # magenta
                print(f'\033[35m{string}\033[m')
            elif color == 'yellow':  # yellow
                print(f'\033[33m{string}\033[m')
            elif color == 'black':  # black
                print(f'\033[30m{string}\033[m')
            
        elif bolder == True:
            if color == 'default':  # white
                print(f'\033[1m{string}\033[m')
            elif color == 'red':  # red
                print(f'\033[1;31m{string}\033[m')
            elif color == 'green':  # green
                print(f'\033[1;32m{string}\033[m')
            elif color == 'blue':  # blue
                print(f'\033[1;34m{string}\033[m')
            elif color == 'cyan':  # cyan
                print(f'\033[1;36m{string}\033[m')
            elif color == 'magenta':  # magenta
                print(f'\033[1;35m{string}\033[m')
            elif color == 'yellow':  # yellow
                print(f'\033[1;33m{string}\033[m')
            elif color == 'black':  # black
                print(f'\033[1;30m{string}\033[m')
    else:
        print(string)

def input_color(color : str='default', bolder : bool=False, input_ini: str='>>>'):
    """A cor do input que você pode desejar

    Args:
        color (str, optional): cor do texto do input (não o que o user digitar). Defaults to 'default'.
        bolder (bool, optional): adiciona um negrito / bolder na fonte. Defaults to False.
        input_ini (str, optional): o que você deseja que seja a string de saida do input. Defaults to '>>>'.

    Returns:
        input: retorna o input para ser adicionada em uma var ou qualquer outra coisa
        
    Color List:
        white;
        red;
        green;
        blue;
        cyan;
        magenta;
        yellow;
        black.
    """

    if bolder == False:
        if color == 'default':  # white
            return input(f'{input_ini} ')
        elif color == 'red':  # red
            return input(f'\033[31m{input_ini}\033[m ')
        elif color == 'green':  # green
            return input(f'\033[32m{input_ini}\033[m ')
        elif color == 'blue':  # blue
            return input(f'\033[34m{input_ini}\033[m ')
        elif color == 'cyan':  # cyan
            return input(f'\033[36m{input_ini}\033[m ')
        elif color == 'magenta':  # magenta
            return input(f'\033[35m{input_ini}\033[m ')
        elif color == 'yellow':  # yellow
            return input(f'\033[33m{input_ini}\033[m ')
        elif color == 'black':  # black
            return input(f'\033[30m{input_ini}\033[m ')
        else:
            print('Isso não foi compreensivel. Veja a doc da função, as cores válidas')
    elif bolder == True:
        if color == 'default':  # white
            return input(f'\033[1m{input_ini}\033[m ')
        elif color == 'red':  # red
            return input(f'\033[1;31m{input_ini}\033[m ')
        elif color == 'green':  # green
            return input(f'\033[1;32m{input_ini}\033[m ')
        elif color == 'blue':  # blue
            return input(f'\033[1;34m{input_ini}\033[m ')
        elif color == 'cyan':  # cyan
            return input(f'\033[1;36m{input_ini}\033[m ')
        elif color == 'magenta':  # magenta
            return input(f'\033[1;35m{input_ini}\033[m ')
        elif color == 'yellow':  # yellow
            return input(f'\033[1;33m{input_ini}\033[m ')
        elif color == 'black':  # black
            return input(f'\033[1;30m{input_ini}\033[m ')
        else:
            print('Isso não foi compreensivel.\nVeja na doc da função (input_color), as cores válidas')
    else:
        print('Não entendi, veja a doc da função (input_color), para utiliza-lá corretamente')
        
def active_venv():
    os.system(r' & .\venv\Scripts\python.exe')
    
    
def move_arquivos(path_origem, path_destino, ext='.pdf'):        
    arquivos_da_pasta_origem = os.listdir(path_origem)
    arquivos = [path_origem + "\\" + f for f in arquivos_da_pasta_origem if ext in f]
    
    for arquivo in arquivos:
        try:
            shutil.move(arquivo, path_destino)
        except shutil.Error:
            shutil.move(arquivo, path_destino)
            os.remove(arquivo)


    
    
def remove_arquivo(file_path : str):
    """ Nota! file_path tem que vir como string real (windows)
    -> r'.\src\myfile.txt'
    """
    os.remove(file_path)
    
def remove_diretorio(dir_path : str):
    """ Nota! file_path tem que vir como string real (windows)
    -> r'.\src\mydir'
    
    Essa função REMOVE DIRETORIOS COM COISAS DENTRO!    
    """
    shutil.rmtree(dir_path)
    
def deixa_arquivos_ocultos_ou_n(path_file_or_dir : str, oculto : bool=True):
    import ctypes
    from stat import FILE_ATTRIBUTE_ARCHIVE
    FILE_ATTRIBUTE_HIDDEN = 0x02

    if oculto:
        ctypes.windll.kernel32.SetFileAttributesW(path_file_or_dir, FILE_ATTRIBUTE_HIDDEN)
    else:
        ctypes.windll.kernel32.SetFileAttributesW(path_file_or_dir, FILE_ATTRIBUTE_ARCHIVE)
        
    # HIDDEN = OCULTO
    # ARCHIVE = Ñ OCULTO
    
    
def ver_tamanho_de_objeto(objeto : object):
    print(sys.getsizeof(objeto))
"""
Iterando sobre as linhas de um dataframe (em uma coluna específica)

for i in df_andamentos_com_todos_os_dados.index:
    print(df_andamentos_com_todos_os_dados['id'][i])

Aqui está acontecendo a iteração sobre um dataframe em pandas que tem a coluna id
e nessa coluna id tem várias linhas
Para cada item in index do dataframe...
"""

def remove_espacos_pontos_virgulas_de_um_int(numero: int, remove_2_ultimos_chars: bool=False):
    numero = str(numero)
    numero = numero.replace(',', '')
    numero = numero.replace('.', '')
    numero = numero.strip()
    if remove_2_ultimos_chars:
        numero = numero[:-2]
    return int(numero)


def remove_arquivo(file_path : str):
    """ Nota! file_path tem que vir como string real (windows)
    -> r'.\src\myfile.txt'
    """
    os.remove(file_path)
    
    
def remove_diretorio(dir_path : str):
    """ Nota! file_path tem que vir como string real (windows)
    -> r'.\src\mydir'
    
    Essa função REMOVE DIRETORIOS COM COISAS DENTRO!    
    """
    shutil.rmtree(dir_path)
    
    
def fecha():
    try:
        quit()
    except NameError:
        pass

    
def fecha_em_x_segundos(qtd_de_segundos_p_fechar : int):
    faz_log(f'Saindo do robô em: {qtd_de_segundos_p_fechar} segundos...')
    for i in range(qtd_de_segundos_p_fechar):
        faz_log(str(qtd_de_segundos_p_fechar))
        qtd_de_segundos_p_fechar -= 1
        sleep(1)
    fecha()
    
    

    
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller 
    
        SE QUISER ADICIONAR ALGO NO ROBÔ BASTA USAR ESSA FUNÇÃO PARA ADICIONAR O CAMINHO PARA O EXECUTÁVEL COLOCAR
        * PARA USAR DEVE COLOCAR ESSA FUNÇÃO NO MÓDULO POR CAUSA DO os.path.abspath(__file__) * 
    """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def times():
    """Dependendo da hora do dia ele fala Bom dia, Boa tarde e Boa noite

    Returns:
        str: Bom dia! or Boa tarde! or Boa noite!
    """
    import datetime
    hora_atual = datetime.datetime.now()
    if hora_atual.hour < 12:
        return 'Bom dia!'
    elif 12 <= hora_atual.hour < 18:
        return 'Boa tarde!'
    else:
        return 'Boa noite!'
