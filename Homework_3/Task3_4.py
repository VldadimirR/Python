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
