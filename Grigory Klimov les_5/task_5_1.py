# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield


def gen_odd(y=15):
    for num in range(1, y + 1, 2):
        yield num


y = 117
x = gen_odd(y)
while True:
    print(next(x))
