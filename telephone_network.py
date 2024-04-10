# АИС для компании RingCell
from registration import register, login


def main():
    while True:
        choice = input("Выберите действие (1 - Регистрация, 2 - Вход, 3 - Выход): ")
        if choice == '1':
            nickname = input("Введите никнейм: ")
            phone = input("Введите телефон: ")
            password = input("Введите пароль: ")
            register(nickname, phone_number, password)
        elif choice == '2':
            nickname = input("Введите никнейм: ")
            phone = input("Введите телефон: ")
            password = input("Введите пароль: ")
            login(nickname, phone_number, password)
        elif choice == '3':
            break
        else:
            print("Ошибка ввода. Попробуйте еще раз.")


if __name__ == '__main__':
    main()
