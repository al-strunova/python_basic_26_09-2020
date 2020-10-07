def int_func(word):
    return word.capitalize()


values = input("Please enter any set of word divided by the space. NOTE: only letters are allowed > ").split(" ")
while not all(e.isalpha() for e in values):
    values = input("Sorry, the value you entered is not valid. "
                   "Please enter any set of word divided by the space. NOTE: only letters are allowed > ")
for i, item in enumerate(values):
    values[i] = int_func(item)
print(" ".join(values))

