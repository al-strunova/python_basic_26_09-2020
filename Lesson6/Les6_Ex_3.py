class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': float(wage), 'bonus': float(bonus)}


class Position(Worker):

    def get_fill_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


employee_1 = Position("John", "Smith", "Manager", 60000, 5000)
employee_2 = Position("Marina", "Jonson", "Team Lead", 45000, 1500)
print(f'{employee_1.get_fill_name()} is a {employee_1.position} '
      f'and he/she has a total income of {employee_1.get_total_income()} $ per year')
print(f'{employee_2.get_fill_name()} is a {employee_2.position} '
      f'and he/she has a total income of {employee_2.get_total_income()} $ per year')
