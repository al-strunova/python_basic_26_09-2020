import json

with open("exercise_7.txt", "r") as f_obj:
    dic = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
    prof_comp = [int(value) for value in dic.values() if value > 0]
    final_dic = [dic, {'average_profit': f'{sum(prof_comp) / len(prof_comp):.2f}'}]
    print(final_dic)
    with open("exercise_7.json", "w", encoding='utf-8') as j_obj:
        json.dump(final_dic, j_obj)


