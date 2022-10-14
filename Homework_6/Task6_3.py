# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

List = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]


def dictionary(List):
    List_1 = list(set(List))
    List_1.sort()
    res = {}
    for name in List_1:
        key = name[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res


print(dictionary(List))

#Вариант 2

# names = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]


# def dict_names(lst):
#     return dict(sorted(((i[0], sorted([j for j in lst if j[0] == i[0]])) for i in lst), key=lambda x: x[0]))


# print(dict_names(names))