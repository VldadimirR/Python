# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
# in
# Number of words: -1
# out
# The data is incorrect
import random

number = int(input('Введите количество слов: '))


def name(number):
    letters = "абв"
    List = []
    for i in range(number):
        b = random.sample(letters, k=3)
        List.append("".join(b))
    result = ' '.join(List)
    return result


def find(my_List):
    my_List = list(filter(lambda x: "абв" not in x, my_List.split()))
    return ' '.join(my_List)


result = name(number)
print(result)
print(find(result))
