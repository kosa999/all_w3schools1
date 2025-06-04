while True:
    password = input("Введите пароль: ")
    if password == "admin123":
        print("Доступ разрешён.")
        break  # выйти из цикла
    else:
        print("Неверный пароль.")
