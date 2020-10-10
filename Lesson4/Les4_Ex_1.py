from sys import argv

_, emp_hours, emp_rate, bonus = argv

print(float(emp_hours) * float(emp_rate) + float(bonus))
