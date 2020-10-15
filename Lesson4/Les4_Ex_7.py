import math


def fact(n):
    for i in range(n):
        yield math.factorial(i)


n = int(input("Please enter any number: "))
for el in fact(n):
    print(el)
