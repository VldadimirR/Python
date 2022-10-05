# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# in
# 650
# out
# [2, 5, 5, 13]


a = int(input("Введите число:"))


def integer_factorization(a):
    List = []
    b = 2
    while b * b <= a:
        while a % b == 0:
            List.append(b)
            a = a / b
        b = b + 1
    if a > 1:
        List.append(a)
    return List


print(integer_factorization(a))
