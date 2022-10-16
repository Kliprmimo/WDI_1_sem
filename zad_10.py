import random

num_list = []
result = 0
while True:
    num = input("podaj liczbe, lub dzialanie: ")
    try:
        num = float(num)
        num_list.append(num)
    except ValueError:
        if num == "+":
            for number in num_list:
                result += number
                num_list = []
            print(result)
        elif num == "-":
            for number in num_list:
                result -= number
                num_list = []
            print(result)
        elif num == "*":
            for number in num_list:
                if result == 0:
                    result = 1
                result *= number
                num_list = []
            print(result)
        elif num == "/":
            for number in num_list:
                if number == 0:
                    result = 0
                if result == 0:
                    result = number
                result /= number
                num_list = []
            print(result)
        elif num == "#":
            for number in num_list:
                if result == 0:
                    result = number
                result = result ** (1 / number)
                num_list = []
            print(result)
        elif num == "^":
            for number in num_list:
                if result == 0:
                    result = number
                result = result ** number
                num_list = []
            print(result)
        elif num == "x":
            x = int(input("podaj mniejsza liczbe z zakresu: "))
            y = int(input("podaj wieksza liczbe z zakresu: "))
            z = random.randrange(x, y)
            print(f"twoja liczba to: {z}")
            num_list.append(z)
        calc_on = input("Czy chcesz wprowadzić nowe dane? T/N ")
        if calc_on == "T":
            continue
        elif calc_on == "N":
            break
