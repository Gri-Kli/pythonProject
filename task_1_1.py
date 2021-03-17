while True:
    duration = (input('Введите количество секунд: '))
    if duration.isdigit():
        duration = int(duration)
        if duration > 0:
            sec = duration % 60
            day = duration // 86400
            remains_hour = duration % 86400 // 3600
            remains_min = duration % 86400 % 3600 // 60
            print('Получилось количество {}дней {}часов {}минут {}секунд'.format(day, remains_hour, remains_min, sec))
            break
