# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988


from decimal import Decimal

a = str(input("Введите число: "))
b = str(input("Введите требуемую точность: "))


def target_accuracy(a, b):
    numberB = Decimal(a)
    number = numberB.quantize(Decimal(b))
    return number


print(target_accuracy(a, b))
