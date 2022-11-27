import random


def finding_coords(n):

    mylist = [[0 for _ in range(n)] for _ in range(n)]
    row_sum = [0] * n
    col_sum = [0] * n
    for x in range(n):
        for y in range(n):
            mylist[x][y] = random.randint(0, 10)
    for x in range(n):
        row_sum[x] = sum(mylist[x])
        for y in range(n):
            col_sum[x] += mylist[y][x]

    quotient = 0
    kol = 0
    coordinates = ()
    for kol_num in col_sum:
        kol += 1
        row = 0
        for row_num in row_sum:
            row += 1
            if quotient < kol_num/row_num:
                quotient = kol_num/row_num
                coordinates = (kol, row)
    return mylist, row_sum, col_sum, coordinates


side_len = 5

usedlist, row_summed, col_summed, cords = finding_coords(side_len)
print('list that we used:')
for num in range(side_len):
    print(usedlist[num])

print(f"columns summed: {col_summed}")
print(f"sum of rows: {row_summed}")
print(f"position of number we are looking for: {cords}")
