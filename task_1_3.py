# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#   print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#   print_hi('PyCharm')

while True:
    percent = input('Введите целое число от 1 до 20 ')
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
    else:
        continue
text_output = 'Вы ввели {} процент{}'.format(percent, anding)
print(text_output)