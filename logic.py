import hashlib
import sqlite3


def after_login_success(nickname):
    connection = sqlite3.connect('telephone_network_db/telephone_network_db.sqlite')
    cursor = connection.cursor()

    cursor.execute("SELECT ID FROM Clients WHERE NickName=?", (nickname,))
    user_id = cursor.fetchone()[0]

    sqlite_select_query_1 = """SELECT FirstName, SecondName, Patronymic, Email, Address FROM Client_Info WHERE ClientID=?"""
    cursor.execute(sqlite_select_query_1, (user_id,))
    records_1 = cursor.fetchall()

    sqlite_select_query_2 = """SELECT PhoneNumber, Balance FROM Client_Devices WHERE ClientID=?"""
    cursor.execute(sqlite_select_query_2, (user_id,))
    records_2 = cursor.fetchall()

    for row_1 in records_1:
        print("Пользователь:", row_1)

    for row_2 in records_2:
        print("Номер телефона, баланс:", row_2)

    connection.close()


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
        after_login_success(nickname)
    else:
        print("Неверное имя пользователя или пароль.")
