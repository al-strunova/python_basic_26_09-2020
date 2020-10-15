with open("exercise_6.txt", "r") as f_obj:
    dic = {}
    for line in f_obj:
        k = line.split(":")[0]
        v = line.split(":")[1].split()
        total = 0
        for i in v:
            if i.find("(") > 0:
                total += int(i.split("(")[0])
        dic[k] = total
    print(dic)
