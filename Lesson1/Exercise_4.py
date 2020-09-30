init_value = int(input('Please enter any positive number > '))
while init_value < 0:
    init_value = int(input('Please enter any positive number > '))
max_num = -1
value = init_value
while value > 0:
    last_digit = value % 10
    value = value // 10
    if last_digit > max_num:
        max_num = last_digit
print(f'{max_num} is the largest digit of the number {init_value}')
