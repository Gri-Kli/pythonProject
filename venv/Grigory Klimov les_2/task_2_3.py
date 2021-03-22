# Сделал как нужно, результат соответсквует заданию
# Под конец написания понял, что можно было написать гораздо проще и понятнее(вырезать из списка числа, положить в переменую
# и отформатировать строку "ф" форматом)
# не стал писать третий вариант решения, боялся не успеть сделать следующие задачи и ознакомится с методичкой к след уроку
########################################################################
true_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while len(true_list) > i:
    element = true_list[i]
    _symbol = element[0]
    if element.isdigit():
        true_list.insert(i, '"')
        i += 1
        if len(element) == 1:
            element = '0' + element[0]
            true_list[i] = element
        else:
            true_list[i] = element
        i += 1
        true_list.insert(i, '"')
    elif _symbol == '+' or _symbol == '-':
        _number = element[1:]
        if _number.isdigit():
            true_list.insert(i, '"')
            i += 1
            element = _symbol + '0' + _number
            true_list[i] = element
            i += 1
            true_list.insert(i, '"')
    else:
        i += 1
true_list = ' '.join(true_list)
true_list = true_list.split('"')
i = 0
for i in range(len(true_list)):
    element = str(true_list[i].strip())
    if element.isdigit() or element[0] == '+' or element[0] == '-':
        true_list[i] = '"' + element + '"'
    else:
        true_list[i] = element
true_list = ' '.join(true_list)
print(true_list)
