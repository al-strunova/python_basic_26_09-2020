class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['{:3}'.format(column) for column in row]) for row in self.matrix])

    def __add__(self, other):
        return Matrix([[self.matrix[row][column] + other.matrix[row][column] for column in range(len(self.matrix[row]))]
                       for row in range(len(self.matrix))])


def sum_res(*args):
    plus = [["", "+"] if r == 1 else ["", ""] for r in range(len(args[0]))]
    equal = [["", "="] if r == 1 else ["", ""] for r in range(len(args[0]))]
    to_return = []
    rows = []

    for row in range(len(args[0])):
        for arg in range(len(args)):
            rows.extend(args[arg][row])
            if arg < len(args) - 2:
                rows.extend(plus[row])
            elif arg == len(args) - 2:
                rows.extend(equal[row])
        to_return.append(rows.copy())
        rows.clear()

    return to_return


# Example 1: 3x2 matrices
matrix1 = Matrix([[2, 3], [4, 1], [7, 9]])
matrix2 = Matrix([[9, 1], [11, 2], [13, 8]])
print(f'Sum of 3x2 matrices: \n{Matrix(sum_res(matrix1.matrix, matrix2.matrix, (matrix1 + matrix2).matrix))}',
      end="\n\n")

# Example 1: 3x3 matrices
matrix1 = Matrix([[1, 2, 3], [3, 4, 1], [6, 7, 9]])
matrix2 = Matrix([[8, 9, 1], [10, 11, 2], [12, 13, 8]])
print(f'Sum of 3x3 matrices: \n{Matrix(sum_res(matrix1.matrix, matrix2.matrix, (matrix1 + matrix2).matrix))}',
      end="\n\n")

# Example 1: 2x4 matrices
matrix1 = Matrix([[1, 2, 3, 6], [3, 4, 1, 9]])
matrix2 = Matrix([[8, 9, 1, 12], [10, 11, 2, 8]])
print(f'Sum of 2x4 matrices: \n{Matrix(sum_res(matrix1.matrix, matrix2.matrix, (matrix1 + matrix2).matrix))}',
      end="\n\n")
