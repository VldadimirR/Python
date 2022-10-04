
import math

a = int(input("Введите число:"))
b = int(input("Введите число:"))

print(a*b//math.gcd(a, b))