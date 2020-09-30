sec = int(input("Please enter any number. This number will be converted from seconds to hh:mm:ss > "))
hours = sec // 3600
minutes = sec % 3600 // 60
seconds = sec % 3600 % 60
print(f'Your output: {hours:02}:{minutes:02}:{seconds:02}')
