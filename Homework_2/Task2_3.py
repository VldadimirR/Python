# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

N = int(input("Введите N: "))

myList = []
for i in range(1, N + 1):
    myList.append(round(((1 + 1/i) ** i)))

sum = 0
for i in range(N):
    sum = sum + myList[i]

print(myList)
print(sum)
