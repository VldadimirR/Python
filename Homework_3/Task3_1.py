#Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
#in
#5
#out
#[10, 2, 3, 8, 9]
#22

from random import sample

amount_of_numbers = int(input('Введите число: '))

def Sum_of_numbers_list_odd_positions(amount_of_numbers):
    arr = sample(range(1, 20), amount_of_numbers )
    print(arr)
    sum = 0
    for i in range(0, len(arr)):
        if i%2 == 0:
            sum = sum + arr[i]
    return sum    

print(Sum_of_numbers_list_odd_positions(amount_of_numbers))
