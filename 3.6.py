

def int_func(a):
    return a.title()
words = input("Input words:").split()
i = 0
while i < len(words):
    words[i] = int_func(words[i])
    i += 1
print(*words)

