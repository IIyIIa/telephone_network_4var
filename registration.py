import hashlib
import sqlite3


def register(nickname, password):
    connection = sqlite3.connect('telephone_network_db/telephone_network_db.sqlite')
    cursor = connection.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM Clients WHERE NickName=?", (nickname,))
    existing_nickname = cursor.fetchone()

    if existing_nickname:
        print("Пользователь с таким никнеймом уже существует.")
        return
    else:
        cursor.execute("INSERT INTO Clients(NickName, Password) "
                       "VALUES (?, ?)",
                       (nickname, hashed_password))
        connection.commit()
        connection.close()
        print("Пользователь зарегистрирован успешно!")


def login(nickname, password):
    connection = sqlite3.connect('telephone_network_db/telephone_network_db.sqlite')
    cursor = connection.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM CLients WHERE  NickName =? AND Password=? ",
                   (nickname, hashed_password))
    result = cursor.fetchone()
    connection.close()
    if result:
        print("Вы успешно вошли в систему!")
    else:
        print("Неверное имя пользователя или пароль.")




