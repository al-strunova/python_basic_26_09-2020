n = int(input("Enter the total number of all elements : "))
lst = [] * n
for i in range(n):
    lst.append(int(input(f"Enter any number to store in the list as {i} element: ")))
new_lst = []
for i in range(n):
    new_lst.append(lst[i])
    if i % 2 != 0:
        new_lst[i-1], new_lst[i] = new_lst[i], new_lst[i-1]
print(new_lst)

