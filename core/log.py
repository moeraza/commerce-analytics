from datetime import date
import logging 


curr_dt = str(date.today()) 

def store_logs(curr_dt=curr_dt,):
    '''
        This permits us to store logs locally, good for development
    '''
    logging.basicConfig(filename='log/{0}.log'.format(curr_dt)
                        ,filemode='a', format='%(asctime)s - %(levelname)s: %(message)s'
                        ,datefmt='%d-%b-%y %H:%M:%S'
                        ,level=logging.INFO
                        )
    logging.info('START LOG')

def stdout_logs():
    '''
        Send logs to standard output
    '''
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
    logger = logging.getLogger(__name__)