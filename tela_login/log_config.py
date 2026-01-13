import logging

logging.basicConfig(filename='app.log',encoding='utf-8', level=logging.DEBUG, format='%(name)s %(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

def get_logger(name):
    return logging.getLogger(name)

if __name__ == '__main__':
    pass
