"""
 definiuje funkcje ktora wypisuje stosunek elementu n+1 do elementu n do momentu w którym ruznica n+1/n - n/n-1
 nie jest wieksza niz 10**-10
 funkcja te przyjmuje 2 liczby,sa to liczby poczatkowe na podstawie ktorych beda wykonywane obliczenia
"""


def fib(x, y):
    num = 1
    while abs(num) > 0.0000000001:
        prev = y / x
        z = x + y
        x = y
        y = z
        print(y/x)
        cur = y/x
        num = prev - cur


print("\nstosunek dla wyrazow 1, 1\n")
fib(1, 1)
print("\nstosunek dla wyrazow 6, 8\n")
fib(6, 8)
print("\nstosunek dla wyrazow 21, 37\n")
fib(21, 37)
print("\nstosunek dla wyrazow 4, 20\n")
fib(4, 20)
