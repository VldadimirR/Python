# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#*Пример:*
# 6 -> да
#- 7 -> да
#- 1 -> нет

a = int(input("Введите номер дня недели: "))
if a >= 1 and a <= 5:
    print ("Это будний день")
elif a >=6 and a <= 7:
    print ("Это выходной")
elif a <= 0 or a >=8:
    print ("Неверное число")        