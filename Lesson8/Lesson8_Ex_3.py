class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


list_ = []
while True:
    try:
        number = input("Enter any positive number to be added to the list. Please type ENTER to stop > ")
        if not number:
            print(f"Final list of previously entered numbers : {list_}")
            break
        if not number.isdigit():
            raise OwnError("Entered value is not a positive numeric number")
    except OwnError as err:
        print(err)
    else:
        list_.append(int(number))
