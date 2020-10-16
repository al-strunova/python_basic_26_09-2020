class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Starting to draw")


class Pen(Stationery):

    def __init__(self):
        super().__init__("Pen")

    def draw(self):
        print(f"Starting to draw with {self.title}\U0001F58A: ------")


class Pencil(Stationery):

    def __init__(self):
        super().__init__("Pencil")

    def draw(self):
        print(f"Starting to draw with {self.title}\u270F\uFE0F: ~~~~~~")


class Handle(Stationery):

    def __init__(self):
        super().__init__("Handle")

    def draw(self):
        print(f"Starting to draw with {self.title}: =======")


obj1 = Pencil()
obj1.draw()
Pen().draw()
Handle().draw()
