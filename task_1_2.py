numbers = []
i = 1
final_number = []
while i <= 1000:
    numbers.append(i)
    i += 2
    numbers_3 = i**3
    final_number.append(numbers_3)
    if final_number[-1] >=1000:
        break
print(numbers)
print(final_number)