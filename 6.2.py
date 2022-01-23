class Road:
    def __init__(self, _length, _width, _mass, _thickness):
        self._length = _length
        self._width = _width
        self._mass = _mass
        self._thickness = _thickness

    def mass(self):
        print(f'нужная масса {self._length * self._width * self._mass * self._thickness / 1000} т')


a = int(input('длина дороги в м '))
w = int(input('ширина дороги в м '))
m = int(input('масса асфальта в кг для покрытия одного кв.метра дороги асфальтом,толщиной 1 см '))
t = int(input('толщина асфальта в см '))
r = Road(a, w, m, t)
r.mass()
