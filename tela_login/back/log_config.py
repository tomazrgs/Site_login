import logging
import os

from dotenv import load_dotenv
load_dotenv()

log_dir = "data" 
log_file = os.path.join(log_dir, "app.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename= log_file,encoding='utf-8',
    level= os.getenv('level'), 
    format='%(name)s %(asctime)s %(message)s', 
    datefmt='%d/%m/%Y %I:%M:%S %p')

def get_logger(name):
    return logging.getLogger(name)

if __name__ == '__main__':
    pass
