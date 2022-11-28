import random


def create_3d(n):
    mylist = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            for z in range(n):
                mylist[x][y][z] = random.randint(10, 99)

    return mylist


def arrange_3d(tab_3d, n):
    size_2d = n ** 2
    list_dims = [[0 for _ in range(n ** 2)] for _ in range(n)]
    i = 0
    dim = 0
    for layer in tab_3d:
        for row in layer:
            for num in row:
                if i < size_2d:
                    list_dims[dim][i] = num
                    i += 1
                else:
                    list_dims[dim+1][0] = num
                    dim += 1
                    i = 1
    for x in range(n):
        list_dims[x].sort()
    return list_dims


def save_positions(list_flat, n):
    sorted_3dlist = []
    for dimention in list_flat:
        list_2dims = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        x = 0
        r = 0
        while x < n ** 2:
            for q in range(n - r * 2):
                if x == n ** 2:
                    break
                list_2dims[r][-(n - q - r)] = dimention[x]
                x += 1

            for w in range(n - r * 2 - 1):
                if x == n ** 2:
                    break
                list_2dims[-(n - 1 - r - w)][-(r + 1)] = dimention[x]
                x += 1

            for e in range(n - r * 2 - 1):
                if x == n ** 2:
                    break
                list_2dims[-(r + 1)][-(e + 2 + r)] = dimention[x]
                x += 1
            for t in range(n - r * 2 - 2):
                if x == n ** 2:
                    break
                list_2dims[-(2 + t + r)][r] = dimention[x]
                x += 1
            r += 1
        sorted_3dlist.append(list_2dims)
    return sorted_3dlist


def run(num):
    table = create_3d(num)
    temp_list = arrange_3d(table, num)
    return save_positions(temp_list, num), table


def index_change(raw, prep, n):
    ind = 0
    for dim in raw:
        print(f"surface {ind}")
        ind += 1
        for row in dim:
            print(row)
    ind2 = 0
    for dim in prep:
        print(f"surface {ind2}")
        ind2 += 1
        for row in dim:
            print(row)

    for x in range(n):
        append_to_file = open('new_file.txt', 'a+')
        surface = f"surface {x}\n"
        append_to_file.write(surface)
        for y in range(n):
            for num in range(10, 100):
                if num in raw[x][y]:
                    old_index = raw[x][y].index(num)
                    for z in range(n):
                        try:
                            new_index = prep[x][z].index(num)
                        except ValueError:
                            continue
                        else:
                            text_to_append = f"({y},{old_index}) -> ({z},{new_index})\n"
                            append_to_file.write(text_to_append)
                            prep[x][z][new_index] = "x"
                            raw[x][y][old_index] = "x"


num2run = 6

done, notdone = run(num2run)

index_change(notdone, done, num2run)
