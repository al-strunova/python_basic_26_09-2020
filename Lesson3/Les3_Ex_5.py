def my_func(previous_sum, items):
    for i in items:
        if i == '*':
            return previous_sum, True
        else:
            previous_sum += int(i)
    return previous_sum, False


flag_to_stop = False
current_sum = 0
while not flag_to_stop:
    values = input("Please enter any set of numbers divided by the space. "
                   "NOTE: you can END at any time by typing > * < character : ").split(" ")
    func_return = my_func(current_sum, values)
    current_sum = func_return[0]
    flag_to_stop = func_return[1]
    print(f">{current_sum}< is the sum of all previously entered values")
