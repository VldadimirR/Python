# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
#[2, 5, 8, 10]
#[20, 40]


from itertools import product
from random import sample

amount_of_numbers = int(input('Введите число: '))


def Sum_of_numbers_list_odd_positions(amount_of_numbers):
    arr = sample(range(1, 10), amount_of_numbers)
    return arr


def Multiplying_first_and_last_element(arr):
    my_List = []
    if len(arr) % 2 == 0:
        length = len(arr)//2
    else:
        length = len(arr)//2 + 1
    for i in range(0, length):
        if i != len(arr)-i-1:
            number = arr[i]*arr[len(arr)-i-1]
        else:
            number = arr[i]
        my_List.append(number)
    return my_List


new_array = Sum_of_numbers_list_odd_positions(amount_of_numbers)
print(new_array)
print(Multiplying_first_and_last_element(new_array))

# Вариант 2
# 2. Напишите программу, которая найдёт произведение пар чисел списка.
#    Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import sample


# def list_rand_nums(count):
#     if count < 0:
#         print("Negative value of the number of numbers!")
#         return []

#     list_nums = sample(range(1, count * 2), count)
#     return list_nums


# def prod_pairs(list_nums: list):
#     res_list = []
#     len_list = len(list_nums)

#     for k in range(len_list // 2):
#         res_list.append(list_nums[k] * list_nums[len_list - k - 1])

#     if len_list % 2:
#         res_list.append(list_nums[len_list // 2])
#     return res_list


# all_list = list_rand_nums(int(input("Number of numbers: ")))
# print(all_list)
# print(prod_pairs(all_list))