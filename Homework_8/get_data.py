

def read():
    with open('Python/Homework_8/cafe.txt', 'r', encoding='utf-8') as my_f:
        directory = my_f.readlines()
        for line in directory:
            print(line.strip())
        print()


def add():
    with open('Python/Homework_8/cafe.txt', 'a', encoding='utf-8') as my_f2:
        line = input('Введите через пробел Имя Фамилия Номер телефона Пол Должность\n')
        my_f2.write(line + '\n')
    return line


def delete():
    with open('Python/Homework_8/cafe.txt', 'r', encoding='utf-8') as my_f3:
        directory = my_f3.readlines()
        marker = 1
        name = input('Введите необходимый номер телефона, запись принадлежащая ему  будет удалена\n')
        with open('Python/Homework_8/cafe.txt', 'w', encoding='utf-8') as my_f:
            for line in directory:
                if name not in line:
                    my_f.write(line)
            if marker:
                print('Указанные данные не найдены')
            return name


def change():
    with open('Python/Homework_8/cafe.txt', 'r', encoding='utf-8') as my_f4:
        directory = my_f4.readlines()
        marker = 1
        name = input('Введите необходимый номер телефона, запись принадлежащая ему  будет изменена\n')
        with open('Python/Homework_8/cafe.txt', 'w', encoding='utf-8') as my_f:
            for line in directory:
                if name in line:
                    marker = 0
                    print(line)
                    new_line = input('Введите через пробел Имя Фамилия Номер_телефона Пол Должность\n')
                    my_f.write(new_line + '\n')
                else:
                    my_f.write(line)
            if marker:
                print('Указанные данные не найдены')
        return name, new_line


def search():
    with open('Python/Homework_8/cafe.txt', 'r', encoding='utf-8') as my_f5:
        directory = my_f5.readlines()
        marker = 1
        name = input('Введите необходимый номер телефона, запись принадлежащая ему будет выведена на экран\n')
        with open('Python/Homework_8/cafe.txt', 'r', encoding='utf-8') as my_f:
            for line in directory:
                if name in line:
                    marker = 0
                    print(line)
            if marker:
                print('Указанные данные не найдены')
        return name
