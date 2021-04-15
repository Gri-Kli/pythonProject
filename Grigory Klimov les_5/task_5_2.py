# Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
max = 15

gen = (x for x in range(1, max + 1, 2))

while True:
    print(next(gen))
