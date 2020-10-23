class ComplexNumber:

    def __init__(self, complex_number):
        self.complex_number = complex_number

    def __add__(self, other):
        return self.complex_number + other.complex_number

    def __mul__(self, other):
        return self.complex_number * other.complex_number


num_1 = ComplexNumber(complex(2, 3))
num_2 = ComplexNumber(complex(3, 5))

print(f'Addition of {num_1.complex_number} and {num_2.complex_number}:'
      f' {num_1.complex_number + num_2.complex_number}')
print(f'Multiplication of {num_1.complex_number} and {num_2.complex_number}:'
      f' {num_1.complex_number * num_2.complex_number}')
