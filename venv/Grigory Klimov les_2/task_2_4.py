# тут все просто
wr_lst = [
    'инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
    'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
for element in wr_lst:
    element = element.split()
    name = element[len(element) - 1]
    _text = f'Привет, {name.title()}!'
    print(_text)