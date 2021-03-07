duration = int(input('Введите количество секунд: '))
sec = duration % 60
min = duration // 60
res_min = min
hour = duration // 3600
day = duration // 86400
remains_hour = duration % 86400 // 3600
remains_min = duration % 86400 % 3600 // 60
print('Получилось количество {}дней {}часов {}минут {}секунд'.format(day, remains_hour, remains_min, sec))