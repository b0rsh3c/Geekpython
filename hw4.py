# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
class TownCar:
    def __init__(self):
        self.speed = 100
        self.color = 'black'
        self.name = 'Town'
        self.is_police = False
    def go(self):
        print('Car is going')
    def stop(self):
        print('Car is stopping')
    def turn(self, direction):
        if direction == 'right':
            print('Car turn to the right')
        elif direction == 'left':
            print('Car turn to the left')
class SportCar:
    def __init__(self):
        self.speed = 200
        self.color = 'red'
        self.name = 'Sport'
        self.is_police = False
    def go(self):
        print('Car is going')
    def stop(self):
        print('Car is stopping')
    def turn(self, direction):
        if direction == 'right':
            print('Car turn to the right')
        elif direction == 'left':
            print('Car turn to the left')
class WorkCar:
    def __init__(self):
        self.speed = 70
        self.color = 'black'
        self.name = 'Work'
        self.is_police = False
    def go(self):
        print('Car is going')
    def stop(self):
        print('Car is stopping')
    def turn(self, direction):
        if direction == 'right':
            print('Car turn to the right')
        elif direction == 'left':
            print('Car turn to the left')
class PoliceCar:
    def __init__(self):
        self.speed = 150
        self.color = 'blue'
        self.name = 'Police'
        self.is_police = True
    def go(self):
        print('Car is going')
    def stop(self):
        print('Car is stopping')
    def turn(self, direction):
        if direction == 'right':
            print('Car turn to the right')
        elif direction == 'left':
            print('Car turn to the left')
mycar = TownCar()
mycar.go()
mycar.stop()
mycar.turn('right')
mycar.turn('left')