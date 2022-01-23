class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __unit__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Всем привет!Меня зовут {self.surname} {self.name}')

    def get_total_income(self):
        print(
            f'я работаю {self.position} и зарабатываю {int(self._income.get("wage")) + int(self._income.get("bonus"))}$$')


surname = input("фамилия сотрудника: ")
name = input("Имя сотрудника: ")
position = input("должность: ")
wage = input("зарплата: ")
bonus = input("премия: ")
a = Position(name, surname, position, wage, bonus)
a.get_full_name()
a.get_total_income()
