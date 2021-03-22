price_list = [57.8, 46.51, 97, 34.50, 5.04, 500.67, 1030.08, 7, 10.10, 14.5]  # создали список цен
for element in price_list:
    if type(element) == int:
        element = float(element)  # преобразуем в вещ. число, если целое
    element = str(element)
    element = element.split('.')  # разбиваем число на руб и коп
    rub = element[0]
    kop = element[1]
    if len(kop) == 1:  # добавляем недостающий нуль
        kop += '0'
    kop = int(kop)
    element = f'{rub} руб {kop:02d} коп,'
    print(element, end='')  # выводим строку по заданию
print()
############################################################
print(price_list[5], 'ID=', id(price_list[5]))  # доказываю, что объект списка после сортировки остался тот же
price_list.sort()
print(price_list[8], 'ID=', id(price_list[8]))
#####################################
for element in price_list:
    if type(element) == int:
        element = float(element)
        # print(element)
    element = str(element)
    element = element.split('.')
    rub = element[0]
    kop = element[1]
    if len(kop) == 1:
        kop += '0'
    kop = int(kop)
    element = f'{rub} руб {kop:02d} коп,'
    print(element, end='')  # вывожу цены отсортированные по возрастанию
print()
##############################################################
price_list.reverse()
price_list_2 = []  # Создаю новый список, содержащий те же цены, но отсортированные по убыванию.
for element in price_list:
    price_list_2.append(element)
######################################################
price_list = price_list_2[:5]
price_list.sort()
for element in price_list:
    if type(element) == int:
        element = float(element)
        # print(element)
    element = str(element)
    element = element.split('.')
    rub = element[0]
    kop = element[1]
    if len(kop) == 1:
        kop += '0'
    kop = int(kop)
    element = f'{rub} руб {kop:02d} коп,'
    print(element, end='')  # Вывожу цены пяти самых дорогих товаров по возрастанию
print()
