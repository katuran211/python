n = int(input("Введите число:"))
list = [9, 8, 7, 7, 7, 6, 4, 2, 2]
m = 0
k = len(list)
if n > list[0]:
    list.insert(0, n)
if n < list[k - 1]:
    list.append(n)
if list[0] >= n >= list[k - 1]:
    while n <= list[m]:
        m += 1
    list.insert(m, n)
print(list)
