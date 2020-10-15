# Open an existing file, count the number of line, count the number of char in each word
with open("exercise_3.txt") as f_obj:
    dic_emp = {}
    emp_under20k = []
    total = 0
    for line in f_obj:
        k, v = line.split()
        dic_emp[k] = float(v)
        total += float(v)
        if float(v) < 20000:
            emp_under20k.append(k)
    print(f'List of employees which salary is less than 20000: {emp_under20k}')
    print(f'Average salary of all employees is: {(total / len(dic_emp)):.2f}')
