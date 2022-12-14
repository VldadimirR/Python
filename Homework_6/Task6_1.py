# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import randint

number = int(input("Введите число: "))


def get_array(number):
    arr = []
    for i in range(number):
        arr.append(randint(0, 30))
    return arr


def numbers_greater_previous(List):
    array = []
    for i in range(1, len(List)):
        if List[i] > List[i - 1]:
            array.append(List[i])
    return array


result = get_array(number)
print(result)
print(numbers_greater_previous(result))
