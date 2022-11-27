import random


def is_prime(a):
    if a < 2:
        return False
    if a == 2 or a == 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    i = 3
    while i * i <= a:
        if a % i == 0:
            return False
        i += 2
        if a % i == 0:
            return False
    return True


def good_or_not_good(number):
    number = str(number)
    size = len(number)
    for digit in range(size):
        if is_prime(int(number[digit])):
            return True
    return False


def new_rand_table(n):
    mylist = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            mylist[x][y] = random.randint(0, 100)

    return mylist


def finding_coords(table):

    lenght = len(table)
    for i in range(lenght):
        check = 0
        for j in range(lenght):
            if good_or_not_good(table[i][j]):
                check += 1
        if check == lenght:
            return True
    return False


while True:
    tablica = new_rand_table(5)
    if finding_coords(tablica):
        for row in tablica:
            print(row)
        break

amount = 0
for _ in range(1000):
    tablica = new_rand_table(5)
    if finding_coords(tablica):
        amount += 1

print(amount/1000)
