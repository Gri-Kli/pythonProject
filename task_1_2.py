
cubic_numbers = []                                          #создаю список кубов
odd_numbers = list(range(1, 1000, 2))                       #создаю список нечетных цифр
for cubic_number in odd_numbers:
    cubic_number **=3
    cubic_numbers.append(cubic_number)
#print(cubic_numbers)                                        #вывел для проверки
good_number_list = []                                       #создал список нечетных кубов которые всецело делятся на 7
number_list = []                                            #создал временный список для сортировки
for number in cubic_numbers:                                #беру каждый элемент списка
    number_x = number
    while number_x > 0:                                     #циклом раскладываю его на составляющие
        number_list.append(number_x % 10)
        number_x //= 10
    if sum(number_list) % 7 == 0:                           #сверяюсь с условиями и при удовлетворении добавляю в список правильных цифр
        good_number_list.append(number)
    number_list.clear()
print(sum(good_number_list))                                #вывожу сумму правильных чисел по задаче 1
i = len(cubic_numbers)
while i != 0:                                               #добавляю "17" к каждому элементу списка
    i -= 1
    cubic_numbers[i] += 17
#print(cubic_numbers)
i = len(cubic_numbers)
while i >= 0:                                               #создаю цикл для редактирования и сортировки элементов списка(не создавая новый список, как указано в задании)
    i -= 1
    number_x = cubic_numbers[i]
    while number_x > 0:
        number_list.append(number_x % 10)
        number_x //= 10
    if sum(number_list) % 7 != 0:
        del cubic_numbers[i]
    number_list.clear()
print(sum(cubic_numbers))                                   #вывожу сумму правильных чисел по задаче 2
