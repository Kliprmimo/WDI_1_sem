num1 = input("podaj pierwsza liczbe: ")
num2 = input("podaj druga liczbe: ")
try:
    num1 = int(num1)
    num2 = int(num2)
    if num2 - num1 > 20:
        num = int(num1+num2/2)
        for x in range(num - 3, num + 4):
            if x != num:
                print(x)
    else:
        for num in range(num1+1, num2):
            print(num)
except ValueError:
    print("to nie sa numery calkowite!")
