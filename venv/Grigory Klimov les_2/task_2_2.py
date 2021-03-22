# Немного запутался в задании( на портале одно, в методичке другое, в презентации третье)
# Сделал с помощью создания нового списка
# В следующем задании, сделал эту же задачу как надо( не создавая нового списка)
true_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
chan_list = []
for element in true_list:
    _symbol = element[
        0]  # перед переменной ставлю "_", имею ввиду временнную переменную(не знаю, правильно ли так делать?)
    if element.isdigit():  # временнную переменную создал для поиска знаков "+" или "-"
        if len(element) == 1:  # добавляю ноль , если его нужно добавлять
            element = '0' + element[0]
            chan_list.extend(['"', element, '"'])
        else:
            chan_list.extend(['"', element, '"'])
    elif _symbol == '+' or _symbol == '-':
        _number = element[1:]
        if _number.isdigit():
            element = _symbol + '0' + _number
            chan_list.extend(['"', element, '"'])
    else:
        chan_list.append(element)
chan_list = ' '.join(chan_list)
print(chan_list)
