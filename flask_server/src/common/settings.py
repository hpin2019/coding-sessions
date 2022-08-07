
DEBUG = 10
INFO = 20
SUCCESS = 25
WARNING = 30
ERROR = 40

DEFAULT_LEVELS = {
    'DEBUG': DEBUG,
    'INFO': INFO,
    'SUCCESS': SUCCESS,
    'WARNING': WARNING,
    'ERROR': ERROR,
}

SERVER_ERROR_TIMER=60
SERVER_PORT = '8081'
#LOG_DIR = '/var/log'
LOG_DIR = './logs/'
LOG_FILE = LOG_DIR+'/server.log'
LOG_FORMAT = '%(asctime)s-%(process)d-%(name)s-%(levelname)s-%(lineno)d-%(message)s'
CONSOLE_LOG_FORMAT = '%(asctime)s-%(process)d-%(name)s-%(levelname)s-%(lineno)d-%(message)s'
FILE_LOG_LEVEL = 'INFO'
CONSOLE_LOG_LEVEL = 'DEBUG'

