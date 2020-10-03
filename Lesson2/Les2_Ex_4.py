user_value = input("Please enter any number of words separating them by space: ")
user_list = user_value.split()
for i in range(len(user_list)):
    print(user_list[i][:10])



