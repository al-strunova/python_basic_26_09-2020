def my_fun1(x, y):
    return x ** y


def my_fun2(x, y):
    for i in range(2, y):
        x *= x


base = float(input("Please enter a base as any positive number : "))
while base < 0:
    base = int(input("Sorry, the value you entered is not valid. "
                     "Please enter a base as any positive number : "))
exponent = int(input("Please enter an exponent as any negative number : "))
while exponent > 0:
    exponent = int(input("Sorry, the value you entered is not valid. "
                         "Please enter an exponent as any negative number : "))
print(f'{base} to the power of {exponent} is {my_fun1(base, exponent):.2f} using x**y method')
print(f'{base} to the power of {exponent} is {my_fun1(base, exponent):.2f} using the loop')
