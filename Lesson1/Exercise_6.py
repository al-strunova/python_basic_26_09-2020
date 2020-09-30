a = int(input('How many kilometers did the sportsman run the first day > '))
b = int(input('How many kilometers was the sportsman supposed to reach > '))

day = 1;
print(f'{day} day : {a}')
while a < b:
    a = a + a * 0.1
    day += 1
    print(f'{day:} day : {a:.2f}')
print(f'{day} day was the day when the sportsman reached the goal - he ran no less than {b} kilometers')
