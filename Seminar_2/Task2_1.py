# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

N = int(input("Введите N: "))

result = 1
for i in range(N):
    print(result, end=" ")
    result *= -3

#вариант 2
#N = int(input("Введите N: "))

#for i in range(N):
#    print(3**k*(-1)**k)
