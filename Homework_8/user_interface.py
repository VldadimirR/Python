import get_data
import error
import log

def interface():
    while True:
        print('1. Вывести базу сотрудников кафе')
        print('2. Добавить запись в базу сотрудников кафе')
        print('3. Удалить запись из базы сотрудников кафе')
        print('4. Изменить запись в базе сотрудников кафе')
        print('5. Найти запись в базе сотрудников кафе ')
        print('6. Для выхода\n')
        print('Ввод')
        operation = error.type_number()

        if operation == 1:
            log.logging.info('Номер выбранного элемента 1')
            get_data.read()

        elif operation == 2:
            log.logging.info('Номер выбранного элемента 2')
            my_add = get_data.add()
            log.logging.info(f'Пользователь ввел: {my_add}')

        elif operation == 3:
            log.logging.info('Номер выбранного элемента 3')
            my_delete = get_data.delete()
            log.logging.info(f'Пользователь ввел: {my_delete}')

        elif operation == 4:
            log.logging.info('Номер выбранного элемента 4')
            my_change = get_data.change()
            log.logging.info(f'Пользователь ввел: {my_change}')

        elif operation == 5:
            log.logging.info('Номер выбранного элемента 5')
            my_search = get_data.search()
            log.logging.info(f'Пользователь ввел: {my_search}')

        elif operation == 6:
            log.logging.info('Конец')
            break

        else:
            print('Вы ввели неверное число')

