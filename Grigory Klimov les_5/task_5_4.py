# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def num_sor(src):
    x = src[0]
    for num in src:
        if num > x:
            x = num
            yield num
        else:
            x = num

g = num_sor(src)
while True:
    print(next(g))
