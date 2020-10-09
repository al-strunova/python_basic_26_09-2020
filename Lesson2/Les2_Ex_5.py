my_list = [7, 5, 3, 3, 2]
nmb_rounds = int(input("Please enter the number of rounds you would like to make to add new ratings: "))
while nmb_rounds <= 0:
    nmb_rounds = int(input("Sorry, the value you entered is not valid. "
                           "Please enter a number of rounds you would like to make to add new ratings: "))
j = 1
while j <= nmb_rounds:
    user_value = int(input(f"Please enter {j} value to be added to {my_list} list: "))
    flag_found = False
    for i in range(len(my_list)):
        if user_value >= my_list[i]:
            my_list.insert(i, user_value)
            flag_found = True
            break
    if not flag_found:
        my_list.append(user_value)
    print(f"The list of ratings was changed to : {my_list}")
    j += 1
print(f"The final list of ratings is : {my_list}")