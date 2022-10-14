# Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь,
# ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"
# out
{'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']},
 'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']},
 'И': {'И': ['Илья Иванов']}, 'В': {'Ю': ['Юнона Ветрякова']}}

def dict_names(lst):
    return dict(sorted(((i[0], sorted([j for j in lst if j[0] == i[0]])) for i in lst), key=lambda x: x[0]))


def dict_second_names(lst):
    return {i.split()[1][0]: dict_names([j for j in lst if i.split()[1][0] == j.split()[1][0]]) for i in lst}

names = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", \
         "Илья Иванов", "Анна Савельева", "Юнона Ветрякова", \
         "Борис Аркадьев", "Антон Серов", "Павел Анисимов"]

print(dict_second_names(names))

# # # Вариант 2

# def thesaurus_adv(*args):
#     s_n_sort = {}
#     for s_n in args:
#         s_n_sort.setdefault(s_n.split()[1][0], {}).setdefault(s_n.split()[0][0], []).append(s_n)
#         return s_n_sort



# print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", \
#          "Илья Иванов", "Анна Савельева", "Юнона Ветрякова", \
#          "Борис Аркадьев", "Антон Серов", "Павел Анисимов"))
