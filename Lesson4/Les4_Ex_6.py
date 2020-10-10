from itertools import count, cycle


def my_func_count():
    value = int(input("Please enter any number less than 10: "))
    for i in count(value):
        if i < 10:
            print(i)
            break

    cnt = 1
    in_list = {"yes", "no", "maybe"}
    for i in cycle(in_list):
        if cnt < value:
            print(i)
            cnt += 1


my_func_count()
