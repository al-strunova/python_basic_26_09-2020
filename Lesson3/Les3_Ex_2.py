def print_user_info(first_name, last_name, age, email, phone):
    print(f'First name: {first_name}, Last name: {last_name}, Age: {age}, Email: {email}, Phone: {phone}')


user_fn = input("Please enter your first name : ")
user_ln = input("Please enter your last name : ")
user_age = input("Please enter your age : ")
user_email = input("Please enter your email : ")
user_phone = input("Please enter your phone number : ")
print_user_info(first_name=user_fn, last_name=user_ln, age=user_age, email=user_email, phone=user_phone)
