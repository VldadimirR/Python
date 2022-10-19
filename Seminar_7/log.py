from datetime import datetime as dt


def universal_logger(data, data_description="действие"):
    """Функция логинит любые данные
    при вызове функции в data_description подставляется строковое описание
    действия(например, 'ввод значения а', 'ввод значения в'), который 
    сопровождает появление переменной data) 
    """
    time = dt.now().strftime('%d-%m-%Y %H:%M:%S')
    with open('Python/Seminar_7/log.csv', 'a', encoding='utf-8') as file:
        file.write('{}; {}; {}\n'
                   .format(time, data_description, data))


def print_log():
    with open('Python/Seminar_7/log.csv', 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
