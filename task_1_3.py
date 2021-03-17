

while True:
    percent = input('Введите целое число от 1 до 20 :  ')
    if percent.isdigit():
        percent = int(percent)
        if percent == 1:
            anding = ''
            break
        elif percent > 1 and percent < 5:
                anding = 'а'
                break
        elif percent > 4 and percent <= 20:
                anding = 'ов'
                break
        else:
            continue

text_output = 'Вы ввели {} процент{}'.format(percent, anding)
print(text_output)