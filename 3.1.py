m = int(input("Введите первое число: "))
n = int(input("Введите второе число: "))


def div(a, b):
    print(f"Деление:{a / b}")


try:
    div(m, n)
except ZeroDivisionError:
    print("Ошибка: Нельзя делить на 0!!!")
