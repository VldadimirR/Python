# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# ou
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q



def encode(my_text):  
    str_code = ''
    count = 1       
    for i in range(len(my_text)):
        if i < len(my_text)-1:
            if my_text[i] == my_text[i + 1]:
                count += 1
            else:
                str_code += str(count) + my_text[i]
                count = 1
        else:
            str_code += str(count) + my_text[i]
    return str_code



def decode(line):
    count = ''
    result = ''
    for i in line:
        if i.isdigit():
            count += i
        else:
            result += i * int(count)
            count = ''
    return result

text = 'aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa'

with open('Homework_5/text_words.txt', 'w') as my_f:
    my_f.write(text)

with open('Homework_5/text_words.txt', 'r') as my_f:
    my_text = my_f.read()


line = encode(my_text)

with open('Homework_5/text_code_words.txt', 'w') as my_f:
    my_f.write(line)

with open('Homework_5/text_code_words.txt', 'r') as my_f:
    my_text = my_f.read()
