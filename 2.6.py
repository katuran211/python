n = int(input("Количество товара:"))
name = []
c = []
k = []
e = []
name2 = []
c2 = []
k2 = []
e2 = []
m = 1
i = 0
f = 0
while m <= n:
    name1 = input(f"Название товара №{m}")
    c1 = int(input(f"Цена товара №{m}"))
    k1 = int(input(f"Количество товара №{m}"))
    e1 = input(f"еденица измерения №{m}")
    name.append(name1)
    c.append(c1)
    k.append(k1)
    e.append(e1)
    m += 1
while i <= (n - 1):
    st = (i + 1, {"Название": name[i], "Цена": c[i], "Количество": k[i], "еденица измерения": e[i]})
    print(st)
    i += 1
while f <= (n - 1):
    name2.append(name[f])
    c2.append(c[f])
    k2.append(k[f])
    e2.append(e[f])
    f += 1
dic = {"Название": name2, "Цена": c2, "Количество": k2, "еденица измерения": e2}
print(dic)
