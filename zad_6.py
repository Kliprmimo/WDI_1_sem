# prosimy uzytkownika o dwie liczby

num1 = input("podaj pierwsza liczbe: ")
num2 = input("podaj druga liczbe: ")

"""
sprawdzamy czy liczby sa liczbami
chcemy uniknac bledu przy zamianie inputu na numer 
"""
try:
    num1 = float(num1)
    num2 = float(num2)
    if num1 < 0 and num2 < 0:
        print("hej! obydwie liczby sa mniejsze od 0!")
    else:
        num1 = abs(num1)
        num2 = abs(num2)
        print(f"suma: {num1 + num2}")
        print(f"ruznica: {num1 - num2}")
        print(f"iloczyn: {num1 * num2}")
        # upewniamy sie ze mozemy wykonac dzielenie
        if num2 != 0:
            print(f"iloraz num1-num2: {num1 / num2}")
        if num1 != 0:
            print(f"iloraz num2-num1: {num2 / num1}")
        print(f"kwadrat num1: {num1 ** 2}")
        print(f"kwadrat num2: {num2 ** 2}")
        print(f"pierwiastek num1: {num1 ** 0.5}")
        print(f"pierwiastek num2: {num2 ** 0.5}")
        if num1 * num2 == 10:
            print("Yay!")
except ValueError:
    print("to nie sa numery!")
# zamieniamy liczy bedace str na int, sprawdzamy czy liczy sa mniejsze niz 0
