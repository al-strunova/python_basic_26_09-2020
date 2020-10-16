import time


class TrafficLight:
    __color = None

    def running(self):
        while True:
            self.__change_color("Red", '\033[101m', 7)
            self.__change_color("Yellow", '\033[103m', 2)
            self.__change_color("Green", '\033[102m', 7)
            self.__change_color("Yellow", '\033[103m', 2)

    def __change_color(self, color, color_bg, wait_time):
        self.__color = color
        print(f'{color_bg}')
        time.sleep(wait_time)


TrafficLight().running()
