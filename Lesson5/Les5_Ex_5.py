import random

with open("exercise_5.txt", "w") as f_obj:
    for number in [random.randrange(1, 10, 1) for _ in range(5)]:
        f_obj.write(f'{number} ')

with open("exercise_5.txt", "r") as f_obj:
    print(sum([int(i) for i in f_obj.read().split()]))
