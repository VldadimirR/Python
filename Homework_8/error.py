
def type_number():
    result = input()
    while type(result) != int:
        try:
            result = int(result)
        except:
            result = input('Вы неверно ввели номер из списка! ')
    return result
