def user_entry():
    return input("Please enter a fruit type. OR you can type ENTER to stop: ")


with open("exercise_1.txt", "w+") as f_obj:
    while True:
        value = user_entry()
        if not value:
            break;
        f_obj.write(f"{value}\n")
