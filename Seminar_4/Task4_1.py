# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.

def check(line):
    arr = line.split()
    for i in arr:
        if not i.strip("-").isdigit():
            return []
    return arr

def search_min_max(array):
    if array:
        return min(array, key=int), max(array, key=int)
    return []

f = check("2 25 -36 ")
print(search_min_max(f))

