def inf(name, surname, year, town, email, phone):
    print(
        f"Меня зовут {surname} {name}. Я родился(ась) в {year} году. Живу в городе {town}. Мой email {email} и номер телефона {phone}")


inf(name=input("Введите ваше имя: "), surname=input("Введите вашу фвамилию: "),
    year=int(input("Введите год вашего рождения: ")), town=input("Введите ваш город проживания: "),
    email=input("Введите ваш email: "), phone=input("Введите номер вашего телефона: "))
