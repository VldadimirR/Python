# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

a = int(input("Введите a "))
b = int(input("Введите b "))
N = int(input("Введите N: "))

myList = []
for i in range(-N, N + 1):
    myList.append(i)

List_Length = N * 2 + 1

if a < List_Length and b <= List_Length:
    multiplication = myList[a-1] * myList[b-1]
    print(myList)
    print(multiplication)
else:
    print('Ошибка! Нарушены границы списка!')