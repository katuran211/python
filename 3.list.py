month = int(input("Номер месяца:"))
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
m = list.index(month)
if m < 2 or m == 11:
    print("Зима")
elif 2 <= m < 5:
    print("Весна")
elif 5 <= m < 8:
    print("Лето")
else:
    print("Осень")
