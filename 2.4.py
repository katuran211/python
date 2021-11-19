list = input("Введите слова:")
lis = list.split()
for n in lis:
    if len(n) < 10:
        print(n)
    else:
        print(n[0:10])
