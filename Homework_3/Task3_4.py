# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
#[5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

import random

number = int(input('Введите число: '))

List = [round(random.uniform(1, 100), 2) for x in range(number)]
print(List)

min = 1
max = 0
for i in List:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)

print('Min:', (round(min, 2)))
print('Max:', (round(max, 2)))
print('Difference:', round(max-min, 2))

# Вариант 2

# from random import uniform


# def list_rand_nums(count: int):
#     list_nums = []
#     if count <= 0:
#         print("Negative value of the number of numbers!")
#         return [0.0]

#     for i in range(count):
#         list_nums.append(round(uniform(1, count), 2))
#     return list_nums


# def dif_max_min(list_nums: list):
#     num_max = num_min = list_nums[0] % 1

#     for k in range(1, len(list_nums)):
#         num = round(list_nums[k] % 1, 2)
#         if num > num_max:
#             num_max = num
#         elif num < num_min:
#             num_min = num

#     result = round(num_max - num_min, 2)
#     print(f"Min: {num_min}, Max: {num_max}. Difference: {result}")
#     return result


# all_list = list_rand_nums(int(input("Number of numbers: ")))
# print(all_list)
# print(dif_max_min(all_list))