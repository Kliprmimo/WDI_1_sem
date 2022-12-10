# Zadanie 6.
# Napisz funkcję, którą umożliwia rekurencyjne generowanie trójkąta Pascala. Użyj adekwatnego formatowania,
# żeby przedstawiany trójkąt rzeczywiście przypominał trójkąt.

row_1 = [1]
row_2 = [1, 1]
pre_row = row_2
size = 15
space_num = size
for _ in range(size+2):
    print("       ", end="")
print(1)
for _ in range(size+1):
    print("       ", end="")
print("1         1")
for num in range(size):
    new_row = [1]
    for i in range(len(pre_row)-1):
        new_row.append(pre_row[i] + pre_row[i+1])
    new_row.append(1)
    pre_row = new_row
    space_num -= 1
    for _ in range(space_num):
        print("       ", end="")
    for index in range(len(new_row)):
        print(f"         {new_row[index]}", end="")
    print("")

