num = int(input("Podaj nieujemną calkowita liczbe: "))

if num == 0:
    print("troche malo zeby hoinke zbudowac")
else:
    i = num - 1
    y = 1
    for x in range(0, num):
        print(" " * i, "*"*y, " " * i)
        i = i - 1
        y = y+2
        if x == num-1:
            print(" "*(num-1), "U", " "*(num-1))
