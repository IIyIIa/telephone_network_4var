# АИС для компании RingCell
from registration import register, login
import sqlite3


def main():
    while True:
        choice = input("Выберите действие (1 - Регистрация, 2 - Вход, 3 - Выход): ")
        if choice == '1':
            nickname = input("Введите никнейм: ")
            phone_number = input("Введите телефон: ")
            password = input("Введите пароль: ")
            register(nickname, phone_number, password)
        elif choice == '2':
            nickname = input("Введите никнейм: ")
            phone_number = input("Введите телефон: ")
            password = input("Введите пароль: ")
            login(nickname, phone_number, password)

            connection = sqlite3.connect('telephone_network_db/telephone_network_db.sqlite')
            cursor = connection.cursor()
            sqlite_select_query = """Select * from Clients"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            for row in records:
                print("Client ID:", row[0])
                print("Nickname:", row[1])
                print("Phone Number:", row[2])

        elif choice == '3':
            break
        else:
            print("Ошибка ввода. Попробуйте еще раз.")


if __name__ == '__main__':
    main()
