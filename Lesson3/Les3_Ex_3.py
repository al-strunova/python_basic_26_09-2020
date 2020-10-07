def my_func(val1, val2, val3):
    my_list = [val1, val2, val3]
    my_list.sort()
    return my_list[1] + my_list[2]


user_value_1 = int(input("Please enter the first value : "))
user_value_2 = int(input("Please enter the second value : "))
user_value_3 = int(input("Please enter the third value : "))
print(f"{my_func(user_value_1, user_value_2, user_value_3)} is the sum of two biggest values")
