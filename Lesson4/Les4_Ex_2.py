init_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([init_list[i] for i in range(1, len(init_list)) if init_list[i] > init_list[i - 1]])
