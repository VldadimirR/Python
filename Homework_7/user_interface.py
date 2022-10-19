import get_data
import error
import log


def interface():
    while True:
        print('1. Вывести телефонный справочник')
        print('2. Добавить запись в телефонный справочник')
        print('3. Удалить запись из справочника')
        print('5. Перевести csv в txt')
        print('4. Для выхода\n')
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

        elif operation == 5:
            log.logging.info('Номер выбранного элемента 5')
            my_creater = get_data.rewriter()
            log.logging.info(f'Пользователь ввел: {my_creater}')

        elif operation == 4:
            log.logging.info('Конец')
            break

        else:
            print('Вы ввели неверное число')
