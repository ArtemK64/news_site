numbers = [1, 4, 6, 7, 9, 12, 12, 13, 15, 234, 237, 240, 246]

for number in numbers:
    if number == 237:
        break
    if number % 2 == 0:
        print(number)
