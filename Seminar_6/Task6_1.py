actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

res = "( 10 + 5 ) * 3 - 8 / 2"


def scob(line):
    lst = []
    i = 0
    while i < len(line):
        if line[i] == '(':
            m = line.index(')', i)
            lst.append(line[i + 1:m])
            i = m
        else:
            lst.append(line[i])
        i += 1
    return lst




def in_scob(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            a, b, c, = scob(lst[i])
            lst[i] = actions[b](a, c)
    return lst


print(in_scob(scob(res.split())))


def result(lst):
    prior = [i for i, j in enumerate(lst) if j in "*/"]
    while prior:
        t = prior[0]
        a, b, c, = lst[t - 1: t + 2]
        lst.insert(t-1, actions[b](a, c))
        del lst[t: t + 3]
        prior = [i for i, j in enumerate(lst) if j in "*/"]
    h = 0
    while len(lst) > 1:
        a, b, c = lst[:3]
        del lst[:3]
        lst.insert(0, actions[b](a, c) ) 
    return lst


print(result(in_scob(scob(res.split()))))

# actions = {
#     "^": lambda x, y: str(float(x) ** float(y)),
#     "*": lambda x, y: str(float(x) * float(y)),
#     "/": lambda x, y: str(float(x) / float(y)),
#     "+": lambda x, y: str(float(x) + float(y)),
#     "-": lambda x, y: str(float(x) - float(y))
# }


# # Ищем скобки, обосабливаем в списки
# def parse(exp_1):
#     pr_list = []
#     i = 0

#     while i < len(exp_1):
#         if exp_1[i] == "(":
#             n_2 = exp_1.index(")", i)
#             pr_list.append(exp_1[i + 1: n_2])
#             i = n_2
#         else:
#             pr_list.append(exp_1[i])
#         i += 1
#     return pr_list


# # Результирующая функция
# # TODO доработать
# def decision(final_list: list):
#     # Получение индексов приоритетных операций
#     ind_list = [i for i, v in enumerate(final_list) if v in "*/"]

#     # Работа с приоритетными операциями
#     while ind_list:
#         k = ind_list[0]
#         a, s, b = final_list[k - 1: k + 2]
#         final_list.insert(k - 1, actions[s](a, b))
#         del final_list[k:k + 3]
#         ind_list = [i for i, v in enumerate(final_list) if v in "*/"]

#     i = 0
#     # Работа с оставшимися операциями
#     while len(final_list) > 2:
#         a, s, b = final_list[:3]
#         del final_list[:3]
#         final_list.insert(i, actions[s](a, b))
#         i = 0

#     return final_list[0]


# # Раскрываем скобки
# def exp_brackets(some_list):
#     for i, v in enumerate(some_list):
#         if isinstance(v, list):
#             some_list[i] = decision(v)
#     return some_list


# # exp = "4 * 3 - 1 / 9 - 7 * -1".split()
# exp = "-2 + ( 4 / 2 - 7 + 8 * 7 ) * 3".split()
# # exp = "( 12 + 8 ) * 3 - 11 / 2".split()
# # exp = "11 / 2 - ( 12 + 8 ) * 3".split()
# # exp = "5 + 11 / 2 - ( 12 + 8 ) * 3 - 12".split()
# # exp = "4 * ( 3 - 1 ) / ( 9 - 7 ) * -1".split()
# # exp = "8 + 2 * 4 + ( 6 + ( 2 - 3 ) * 2 )".split()  # 1

# pr_list = exp_brackets(parse(exp))
# print(pr_list)
# print(decision(pr_list))