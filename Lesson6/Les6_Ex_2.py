class Road:
    __thickness = 5
    __weight_density = 0.025

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_asphalt_weight(self):
        print(f'To cover {self._width} x {self._length} square metres area, you need : '
              f'{self._length * self._width * self.__thickness * self.__weight_density:.2f} tonne(s) of asphalt')


Road(20, 5000).calculate_asphalt_weight()
