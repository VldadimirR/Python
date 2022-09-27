# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
#    где k принимает значения от 1 до n включительно.

N = int(input("Введите N: "))
myList = []
for k in range (1,N+1):
    myList.append(3*k + 1)
print(myList)
