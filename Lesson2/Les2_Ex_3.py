season_month_map = {1: 'Winter', 2: 'Winter', 3: 'Winter',
                    4: 'Spring', 5: 'Spring', 6: 'Spring',
                    7: 'Summer', 8: 'Summer', 9: 'Summer',
                    10: 'Fall', 11: 'Fall', 12: 'Winter'}
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
user_value = int(input("Please enter any number from 1 to 12 : "))
while user_value < 1 or user_value > 12:
    user_value = int(input("Sorry, the value you entered is not valid. Please enter any number from 1 to 12 : "))
print(
    f"#{user_value} month of the year is {month_list[user_value - 1]}, "
    f"and the season when it happens is {season_month_map[user_value]}")
