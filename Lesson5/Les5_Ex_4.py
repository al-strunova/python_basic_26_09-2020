dic_translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file_init = open("exercise_4_init.txt", "r")
file_updated = open("exercise_4_updated.txt", "w")

for line in file_init:
    new_value = f'{dic_translate[line.split()[0]]} - {line.split()[2]}'
    print(new_value)
    file_updated.write(f'{new_value}\n')

file_init.close()
file_updated.close()