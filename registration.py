import hashlib
import sqlite3


def register(nickname, phone_number, password):
    connection = sqlite3.connect('telephone_network_db/telephone_network_db.sqlite')
    cursor = connection.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM Clients WHERE NickName=?", (nickname,))
    existing_nickname = cursor.fetchone()
    cursor.execute("SELECT * FROM Clients WHERE PhoneNumber=?", (phone_number,))
    existing_phone_number = cursor.fetchone()

    if existing_nickname:
        print("Пользователь с таким никнеймом уже существует.")
        return
    if existing_phone_number:
        print("Пользователь с таким номером телефона уже существует.")
        return
    else:
        cursor.execute("INSERT INTO Clients(NickName, PhoneNumber, Password) "
                       "VALUES (?, ?, ?)",
                       (nickname, phone_number, hashed_password))
        connection.commit()
        connection.close()
        print("Пользователь зарегистрирован успешно!")


def login(nickname, phone_number, password):
    connection = sqlite3.connect('telephone_network_db/telephone_network_db.sqlite')
    cursor = connection.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM CLients WHERE  NickName =? AND PhoneNumber=? AND Password=? ",
                   (nickname, phone_number, hashed_password))
    result = cursor.fetchone()
    connection.close()
    if result:
        print("Вы успешно вошли в систему!")
    else:
        print("Неверное имя пользователя или пароль.")

