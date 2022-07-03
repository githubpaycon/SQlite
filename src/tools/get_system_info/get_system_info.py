import psutil
import platform
from datetime import datetime
import socket
import uuid
import re
from src.tools.log.log_manager import faz_log

"""
Necessário ter a função faz_log
https://stackoverflow.com/questions/3103178/how-to-get-the-system-info-with-python
"""

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def System_information():
    faz_log("==== INFORMAÇÃO DO SISTEMA ====")
    uname = platform.uname()
    faz_log(f"SISTEMA: {uname.system}")
    
    faz_log(f"NOME DO PC: {uname.node}")
    
    faz_log(f"VERSÃO DO SISTEMA: {uname.release}")
    
    faz_log(f"VERSÃO DO SISTEMA (COMPLETO): {uname.version}")
    faz_log(f"ARQUITETURA: {uname.machine}")
    faz_log(f"PROCESSADOR: {uname.processor}")
    faz_log(f"ENDEREÇO IP: {socket.gethostbyname(socket.gethostname())}")
    faz_log(f"ENDEREÇO MAC: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}")


    # Boot Time
    faz_log("==== HORA QUE LIGOU O COMPUTADOR ====")
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    faz_log(f"HORA DO BOOT: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")


    # print CPU information
    faz_log("==== INFOS DA CPU ====")
    # number of cores
    faz_log(f"NÚCLEOS FÍSICOS: {psutil.cpu_count(logical=False)}")
    faz_log(f"TOTAL DE NÚCLEOS: {psutil.cpu_count(logical=True)}")
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    faz_log(f"FREQUÊNCIA MÁXIMA: {cpufreq.max:.2f}Mhz")
    faz_log(f"FREQUÊNCIA MÍNIMA: {cpufreq.min:.2f}Mhz")    
    faz_log(f"FREQUÊNCIA ATUAL: {cpufreq.current:.2f}Mhz")
    # CPU usage
    faz_log("USO DA CPU POR NÚCLEO:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        faz_log(f"NÚCLEO {i}: {percentage}%")
    faz_log(f"USO TOTAL DA CPU: {psutil.cpu_percent()}%")


    # Memory Information
    faz_log("==== INFOS DA MEMÓRIA RAM ====")
    # get the memory details
    svmem = psutil.virtual_memory()
    faz_log(f"MEMÓRIA RAM TOTAL: {get_size(svmem.total)}")
    faz_log(f"MEMÓRIA RAM DISPONÍVEL: {get_size(svmem.available)}")
    faz_log(f"MEMÓRIA RAM EM USO: {get_size(svmem.used)}")
    faz_log(f"PORCENTAGEM DE USO DA MEMÓRIA RAM: {svmem.percent}%")


    ## Network information
    faz_log("==== INFORMAÇÕES DA INTERNET ====")
    ## get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            faz_log(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                faz_log(f"  ENDEREÇO IP: {address.address}")
                faz_log(f"  MASCARÁ DE REDE: {address.netmask}")
                faz_log(f"  IP DE TRANSMISSÃO: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                faz_log(f"  ENDEREÇO MAC: {address.address}")
                faz_log(f"  MASCARÁ DE REDE: {address.netmask}")
                faz_log(f"  MAC DE TRANSMISSÃO: {address.broadcast}")
    ##get IO statistics since boot
    net_io = psutil.net_io_counters()
    faz_log(f"TOTAL DE Bytes ENVIADOS: {get_size(net_io.bytes_sent)}")
    faz_log(f"TOTAL DE Bytes RECEBIDOS: {get_size(net_io.bytes_recv)}")


if __name__ == "__main__":
    
    System_information()
