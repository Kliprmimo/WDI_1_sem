# Zadanie 3.
# Dana jest tablica zawierająca liczby wymierne. Proszę napisać funkcję, która policzy występujące w tablicy
# ciągi arytmetyczne (LA) i geometryczne (LG) o długości większej niż 2.
# Funkcja powinna zwrócić wartość 1 gdy LA>LG, wartość −1 gdy LA<LG oraz 0 gdy LA==LG.
my_list_0 = [1, 2, 3, 4, 5, 6, 7, -2, 1, -1 / 2, 1 / 4]
my_list_1 = [2, 1, 3, 7, 8, 4, 2, 1, 1 / 2, 1 / 4, 1 / 8, 4 / 8, 7 / 8, 10 / 8, 13 / 8, 2, 19 / 8]
my_list_2 = [2 / 3, 1 / 3, 0, -1 / 3, -2 / 3, -1, -4 / 3, -16 / 9, -64 / 27, -256 / 81, -1024 / 243, -4096/729, -16384/2187]


def check_for_series(list_to_check):
    k = 2
    len_lg = 2
    len_la = 2
    for i in range(len(list_to_check)):
        try:
            if list_to_check[i] * list_to_check[i + 2] == list_to_check[i + 1] ** 2:
                quotient = list_to_check[i + 1] / list_to_check[i]
                while round(list_to_check[i + k] * quotient, 13) == round(list_to_check[i + 1 + k], 13):
                    k += 1
                    if len_lg < k + 1:
                        len_lg = k + 1
                k = 2
        except IndexError:
            continue
    k = 2
    for i in range(len(list_to_check)):
        try:
            if list_to_check[i] + list_to_check[i + 2] == list_to_check[i + 1] * 2:
                diff = list_to_check[i + 1] - list_to_check[i]
                while list_to_check[i + k] + diff == list_to_check[i + 1 + k]:
                    k += 1
                    if len_la < k + 1:
                        len_la = k + 1
                k = 2
        except IndexError:
            continue

    print(f"lenght of arithmetic sequence = {len_la}")
    print(f"lenght of  geometric sequence = {len_lg}")
    if len_la > len_lg:
        return 1
    elif len_la < len_lg:
        return -1
    elif len_la == len_lg:
        return 0


print(check_for_series(my_list_0))
print(check_for_series(my_list_1))
print(check_for_series(my_list_2))
