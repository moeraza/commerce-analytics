import configparser
import datetime
from core.log import *

def get_configs():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if config['ANALYSIS']['TEST_MODE'] in [True, 'True','y','yes','Yes']:
        TEST_MODE = True
        logging.info('Running in test mode, will only use a subset of the dataset')
    else:
        TEST_MODE = False
        logging.info('Running in full mode, will use full data set')
    return TEST_MODE

def convert_time_stamp(x):
    '''
        Convert from seconds to X days HH:MM:SS
    '''
    return str(datetime.timedelta(seconds=x))
