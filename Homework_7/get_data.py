
import csv


def read():
    with open('Python/Homework_7/phonebook.csv', 'r', encoding='utf-8') as my_f:
        directory = my_f.readlines()
        for line in directory:
            print(line.strip())
        print()


def add():
    with open('Python/Homework_7/phonebook.csv', 'a', encoding='utf-8') as my_f2:
        line = input(
            'Введите через пробел Имя Фамилия Номер_телефона Описание\n')
        my_f2.write(line + '\n')
    return line


def delete():
    with open('Python/Homework_7/phonebook.csv', 'r', encoding='utf-8') as my_f3:
        directory = my_f3.readlines()
        marker = 1
        name = input(
            'Введите необходимый номер телефона, запись принадлежащая ему  будет удалена\n')
        with open('Python/Homework_7/phonebook.csv', 'w', encoding='utf-8') as my_f:
            for line in directory:
                if name not in line:
                    my_f.write(line)
            if marker:
                print('Указанные данные не найдены')
        return name


def rewriter():
    with open('Python/Homework_7/phonebook.txt', 'w', encoding='utf-8') as my_output_file:
        with open('Python/Homework_7/phonebook.csv', 'r', encoding='utf-8') as my_input_file:
            [my_output_file.write(' '.join(row)+'\n')
             for row in csv.reader(my_input_file)]
        print('Перевод завершен')
