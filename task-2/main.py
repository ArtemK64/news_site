input_number = float(input("Введите число: "))
input_limit = float(input("Введите пограничное число: "))

if input_number < input_limit:
    print("Введенное число меньше пограничного.")
elif input_number > input_limit:
    print("Введенное число больше пограничного.")
    if input_number > input_limit * 3:
        print("Введенное число больше пограничного более, чем в 3 раза.")
else:
    print("Введенное число равно пограничному числу.")