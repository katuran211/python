d = int(input("Введите первое число: "))
f = int(input("Введите второе число: "))
g = int(input("Введите третье число: "))


def my_func(a, b, c):
    m = max(a, b, c)
    if m == a:
        n = max(b, c)
        return m + n
    if m == b:
        n2 = max(a, c)
        return m + n2
    if m == c:
        n3 = max(a, b)
        return m + n3


print(f"Сумма двух наибольших чисел: {my_func(d, f, g)}")
