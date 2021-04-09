# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо
# вывести последние кортежи в виде: (<tutor>, None)
# по окончании скрипта в консоле появляетя ошибка, свидетельство того, что генератор истощился(как Я понял ))

tutors = ["Иван", "Анастасия", "Петр", "Сергей", "Дмитрий", "Борис", "Елена"]
klasses = ["9А", "7В", "9Б", "9В", "8Б"]  # , "10А", "10Б", "9А"]


def gen_tup(tutors, klasses):
    for i in range(len(tutors)):
        klasses_len = len(klasses)
        if i >= klasses_len:
            fin_tup = (tutors[i], "None")
            yield fin_tup
        else:
            fin_tup = (tutors[i], klasses[i])
            yield fin_tup


x = gen_tup(tutors, klasses)
while True:
    print(next(x))
