def my_sum():
    sum_res = 0
    ex = False
    while ex == False:
        number = input("Введите числа или Q (чтобы заверишить программу)").split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break

            else:
                try:
                    res = res + int(number[el])
                except ValueError:
                    res = 0
                    for r in range(len(number)):
                        number[r] = 0
                    print("Ошибка:Неккоректно введены числа/число!!!")
        sum_res = sum_res + res
        print(f'Текущий результат:  {sum_res}')
    print(f'Окончательный результат: {sum_res}')


my_sum()
