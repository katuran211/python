class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def Go(self):
        return f'{self.name} поехала'

    def Stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return self.speed

    def police(self):
        if self.is_police:
            return f'{self.name} - ДА'
        else:
            return f'{self.name} - НЕТ'


class TownCar(Car):
    def __unit__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'скорость {self.name} превышенв!!!')
        else:
            return self.speed


class WorkCar(Car):
    def __unit__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'скорость {self.name} превышенв!!!')
        else:
            return self.speed


class PoliceCar(Car):
    def __unit__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):
    def __unit__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


name1 = input('Марка легковой  машины')
color1 = input('Цвет легковой машины')
speed1 = input('Скорость легковой машины')
name2 = input('Марка рабочей машины')
color2 = input('Цвет рабочей машины')
speed2 = input('Скорость рабочей машины')
name3 = input('Марка полицейской машины')
color3 = input('Цвет полицейской машины')
speed3 = input('Скорость полицейской машины')
name4 = input('Марка спорт  машины')
color4 = input('Цвет спорт машины')
speed4 = input('Скорость спорт машины')

a = TownCar(speed1, color1, name1, False)
b = WorkCar(speed2, color2, name2, True)
c = PoliceCar(speed3, color3, name3, True)
d = SportCar(speed4, color4, name4, False)
a.turn_left()
print(f'{c.name} полицеская машина? {c.police()}')
print(f'{a.name} полицеская машина? {a.police()}')
print(f'После того как {b.turn_right()}, {c.Stop()}')
print(f'{c.Go()} со скоростью {c.speed}')
print(f'{c.name} {c.color} цвета')
print(f'скорость {a.name} - {a.speed} км/ч')
print(f'скорость {b.name} - {b.speed} км/ч')
print(f'скорость {c.name} - {d.speed} км/ч')
