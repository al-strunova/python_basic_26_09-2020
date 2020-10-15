def user_entry():
    return input("Please enter a name of the book you would like to read. It will be added to the 'Reading List'. "
                 "You can type ENTER when you are done: ")


# Add a new file and save some data
with open("exercise_2.txt", "w") as f_obj:
    flag_to_stop = False
    while not flag_to_stop:
        value = user_entry()
        if not value:
            flag_to_stop = True
        if not flag_to_stop:
            f_obj.write(f"{value}\n")
        else:
            break

# Open an existing file, count the number of line, count the number of char in each word
with open("exercise_2.txt") as f_obj:
    nbr_lines = 1
    for line in f_obj:
        print(f'{nbr_lines} line > {line}', end="")
        print(f'It contains {len(line.split())} words')
        nbr_lines += 1
    print(f'Total line(s) in {f_obj.name} file: {nbr_lines}')
