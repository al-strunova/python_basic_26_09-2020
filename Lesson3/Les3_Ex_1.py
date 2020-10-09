def division(dividend, divisor):
    return dividend / divisor


user_dividend = int(input("Please enter a dividend : "))
user_divisor = int(input("Please enter a divisor : "))
while user_divisor == 0:
    user_divisor = int(input("Sorry, division by zero is undefined. Please enter a valid divisor : "))
quotient = division(user_dividend, user_divisor)
print(f"{user_dividend} / {user_divisor} = {quotient:.2f}")
