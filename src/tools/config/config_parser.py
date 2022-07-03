from configparser import RawConfigParser
from src.tools.ui.windows import Windows
from src.tools.log.log_manager import faz_log
import os
windows = Windows()

class ConfigParserClaro:
    @staticmethod
    def config_read():
        faz_log('Lendo configurações...')
        PATH_CONFIG = os.path.abspath(r'.\.bin\config.ini')
        configs = RawConfigParser()
        configs.read(PATH_CONFIG)

        # retorna o config como dict
        config = {s:dict(configs.items(str(s))) for s in configs.sections()}
        return config
