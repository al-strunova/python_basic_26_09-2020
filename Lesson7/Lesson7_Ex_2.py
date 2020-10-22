from abc import ABC, abstractmethod


class Cloth(ABC):

    @abstractmethod
    def material_usage(self):
        pass


class Coat(Cloth):

    def __init__(self, size):
        self.size = float(size)

    @property
    def material_usage(self):
        return round((self.size / 6.5 + 0.5), 2)


class Suit(Cloth):

    def __init__(self, length):
        self.length = float(length)

    @property
    def material_usage(self):
        return round((2 * self.length + 0.3), 2)


coat = Coat(2)
suit = Suit(10)

print(f"Material usage for a coat: {coat.material_usage}")
print(f"Material usage for a suit: {suit.material_usage}")
print(f"Total usage for both coat and a suit: {coat.material_usage + suit.material_usage}")
