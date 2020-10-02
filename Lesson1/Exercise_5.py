revenue = int(input('Please enter your company\'s revenue > '))
expenses = int(input('Please enter your company\'s expenses > '))
profit = revenue - expenses
if profit >= 0:
    print(f'Congratulation! Your company is profitable.')
    print(f'Your net income is {profit}')
    npm = profit / revenue
    print(f'The net profit margin is {npm}')
    num_of_employees = int(input('Please enter the number of your employees > '))
    ppe = profit / num_of_employees
    print(f'The profit per employee is {ppe}')
else:
    print(f'Sorry! Your company is NOT profitable.')