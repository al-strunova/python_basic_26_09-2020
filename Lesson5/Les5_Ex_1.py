def user_entry():
    return input("Please enter a fruit type. OR you can type ENTER to stop: ")


with open("exercise_1.txt", "w+") as f_obj:
    flag_to_stop = False
    while not flag_to_stop:
        value = user_entry()
        if not value:
            flag_to_stop = True
        if not flag_to_stop:
            f_obj.write(f"{value}\n")
        else:
            break
