from random import choice


class Car:

    def __init__(self, speed, color, name, car_type, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.type = car_type
        self.is_police = is_police

    def go(self):
        print(f'{self.type} - {self.name} - {self.color} is starting to move.')
        if self.is_police:
            print("Please note, it a Police car")

    def stop(self):
        print(f'{self.type} - {self.name} - {self.color} stopped')

    def turn(self, direction):
        print(f'{self.type} - {self.name} - {self.color} turns to the {direction}')

    def show_speed(self):
        print(f'The current speed for {self.type} - {self.name} - {self.color} is {self.speed} mph')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'The current speed for {self.type} - {self.name} - {self.color} '
                  f'is {self.speed} mph which is MORE THAN ALLOWED')
        else:
            print(f'The current speed for {self.type} - {self.name} - {self.color} is {self.speed} mph')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'The current speed for {self.type} - {self.name} - {self.color} '
                  f'is {self.speed} mph which is MORE THAN ALLOWED')
        else:
            print(f'The current speed for {self.type} - {self.name} - {self.color} is {self.speed} mph')


class PoliceCar(Car):
    pass


cars = [TownCar(50, "Black", "Volkswagen Beetle", "Town Car"),
        TownCar(70, "Red", "Chevrolet Corvette", "Town Car"),
        PoliceCar(80, "White", "Volkswagen Beetle", "Police Car", True),
        WorkCar(50, "Silver", "Honda Fit", "Work Car"),
        WorkCar(40, "Black", "Jeep Cherokee", "Work Car"),
        SportCar(90, "Black", "Jaguar FX", "Sport Car")]
turns = ["right", "left"]

for car in cars:
    print('*' * 30)
    car.go()
    car.turn(choice(turns))
    car.show_speed()
    car.stop()
    print('*' * 30)
