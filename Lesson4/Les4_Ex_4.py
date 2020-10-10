init_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
dict = {}
for i in init_list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

init_list = [i for i in init_list if dict[i] < 2]
print(init_list)
