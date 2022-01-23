from time import sleep

print("Светофор работает 4 минуты")


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 6:
            print(f'{TrafficLight.__color[2]} - 31 сек.')
            sleep(31)
            print(f'{TrafficLight.__color[0]} - 7 сек.')
            sleep(7)
            print(f'{TrafficLight.__color[1]} - 2 сек.')
            sleep(2)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
