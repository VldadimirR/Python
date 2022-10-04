# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011

number = int(input('Введите число: '))

list = []

while number > 0:
    result = (number % 2)
    list.append(result)
    number = number // 2

list.reverse()
print(list)

# Вариант 2
# def conv_bin(num: int):
#     list_nums = []

#     while num > 0:
#         list_nums.insert(0, num % 2)
#         num //= 2

#     print(*list_nums, sep="")


# conv_bin(int(input()))
