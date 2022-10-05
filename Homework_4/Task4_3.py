# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


from random import randint

number = int(input("Введите число: "))


def get_array(number):
    arr = []
    for i in range(number):
        arr.append(randint(0, 9))
    return arr


def non_repeating_numbers(List):
    array = []
    for i in List:
        if List.count(i) < 2:
            array.append(i)
    return array


if number > 0:
    array = get_array(number)
    print(array)
    print(non_repeating_numbers(array))
else:
    print('Вы ввели неверное значение')
