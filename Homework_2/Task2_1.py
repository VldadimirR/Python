# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27
n = float(input("Введите число: "))

number_length = len(str(n))
converted_number = n * 10 ** (number_length - 2)

sum = 0
while converted_number > 0:
    sum += converted_number % 10
    converted_number //= 10
print(round(sum))
