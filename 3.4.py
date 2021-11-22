x = int(input("Введите x: "))
y = int(input("Введите y: "))


def my_func (a, b):
    i = 1
    m = 1
    while i <= abs(b):
        m *= a
        i += 1
    return 1 / m


print(f"{x} в степени {y} = {my_func(x, y)}")
