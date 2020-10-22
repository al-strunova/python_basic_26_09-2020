class Cell:

    def __init__(self, cell):
        self.cell = int(cell)

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        return abs(self.cell - other.cell)

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        return self.cell // other.cell

    def make_order(self, rows):
        total = self.cell
        str = ""
        while total >= 0:
            if int(total) - int(rows) >= 0:
                str += '*' * rows + '\n'
            else:
                str += '*' * total
            total = int(total) - int(rows)
        return str


cell_1 = Cell(8)
cell_2 = Cell(2)
rows = 3
print(f'First cell: {cell_1.cell} cells, {rows} rows: \n{cell_1.make_order(rows)}')
print(f'Second cell: {cell_2.cell} cells, {rows} rows: \n{cell_2.make_order(rows)}')
print(f'Sum of {cell_1.cell} and {cell_2.cell} cells: {cell_1 + cell_2} cells, {rows} rows:'
      f' \n{Cell(cell_1 + cell_2).make_order(rows)}')
print(f'Subtraction of {cell_1.cell} and {cell_2.cell} cells: {cell_1 - cell_2} cells, {rows} rows:'
      f' \n{Cell(cell_1 - cell_2).make_order(rows)}')
print(f'Multiplication of {cell_1.cell} and {cell_2.cell} cells: {cell_1 * cell_2} cells, {rows} rows:'
      f' \n{Cell(cell_1 * cell_2).make_order(rows)}')
print(f'Division of {cell_1.cell} and {cell_2.cell} cells: {cell_1 // cell_2} cells, {rows} rows:'
      f' \n{Cell(cell_1 // cell_2).make_order(rows)}')
