list = input("Enter list:").split()
m = len(list)
lis = list.copy()
i = 0
if m % 2 == 0:
    while i < m:
        lis[i] = list[i + 1]
        lis[i + 1] = list[i]
        i += 2
else:
    while i <= (m - 2):
        lis[i] = list[i + 1]
        lis[i + 1] = list[i]
        i += 2
print(lis)
