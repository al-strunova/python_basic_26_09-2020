class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def split_date(cls, obj):
        date = obj.date
        date = {"day": int(date.split('-')[0]),
                "month": int(date.split('-')[1]),
                "year": int(date.split('-')[2])}
        if cls.validate_date(date):
            print(f"User's birthday is VALID: {date}\n")

    @staticmethod
    def validate_date(date):
        if date["day"] < 1 or date["day"] > 31:
            print(f"ERROR: Day > {date['day']} is invalid. The valid date is between 1 and 31.\n")
            return False
        if date["month"] < 1 or date["month"] > 12:
            print(f"ERROR: Month > {date['month']} is invalid. The valid month is between 1 and 12.\n")
            return False
        if date["year"] < 1900 or date["year"] > 2021:
            print(f"ERROR: Year > {date['year']} is invalid. The valid year is between 1900 and 2020.\n")
            return False
        return True


users = [Date("11-01-1991"), Date("32-01-1991"), Date("11-14-1991"), Date("11-01-1899")]

for i in range(len(users)):
    print(f">{users[i].date}< is the #{i + 1} user's birthday to validate:")
    Date.split_date(users[i])
