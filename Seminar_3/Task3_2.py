
from random import choices


def name(a, b):
    List = []
    for i in range(a):
        c = choices(b, k=3)
        List.append("".join(c))
    return List


my_List = name(10, "xyz")
print(my_List)


def find(d, f):
    if d in f and f.count(d) > 1:
        g = f.index(d)
        print(f.index(d, g + 1))
    else:
        print(-1)
find(input(),my_List)


