class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        dividend = float(input("Enter a dividend: "))
        divisor = float(input("Enter a divisor: "))
        if divisor == 0:
            raise OwnError("A dividend can't be divided by zero")
    except OwnError as err:
        print(err)
    else:
        print(f"{dividend} / {divisor} = {dividend / divisor:.2f}")
        break
