import logging

logging.basicConfig(
    level=logging.INFO, filename='Python/Homework_7/phonebook.log',
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S', encoding='utf-8')
