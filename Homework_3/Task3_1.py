# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
#[10, 2, 3, 8, 9]
# 22

from random import sample

amount_of_numbers = int(input('Введите число: '))


def Sum_of_numbers_list_odd_positions(amount_of_numbers):
    arr = sample(range(1, 20), amount_of_numbers)
    print(arr)
    sum = 0
    for i in range(0, len(arr)):
        if i % 2 == 0:
            sum = sum + arr[i]
    return sum


print(Sum_of_numbers_list_odd_positions(amount_of_numbers))

# Вариант 2

# from random import sample


# def list_rand_nums(count: int):
#     if count < 0:
#         print("Negative value of the number of numbers!")
#         return []

#     list_nums = sample(range(1, count * 2), count)
#     return list_nums


# def sum_odd_pos(list_nums: list):
#     sum_nums = 0
#     for k in range(0, len(list_nums), 2):
#         sum_nums += list_nums[k]
#     return sum_nums


# all_list = list_rand_nums(int(input("Number of numbers: ")))
# print(all_list)
# print(sum_odd_pos(all_list))

