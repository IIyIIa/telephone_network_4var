import hashlib
import sqlite3
import sys
from telephone_network_db.alchemy.database import session_factory
from telephone_network_db.alchemy.orm import ClientsORM


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
    session = session_factory()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    existing_nickname = session.query(ClientsORM).filter(ClientsORM.NickName == nickname).first()

    if existing_nickname:
        print("Пользователь с таким никнеймом уже существует.")
        return
    else:
        client_registrate = ClientsORM(NickName=nickname, Password=hashed_password)
        session.add(client_registrate)
        session.commit()
        session.close()
        print("Пользователь зарегистрирован успешно!")


def login(nickname, password):
    session = session_factory()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    client_nickname_check = session.query(ClientsORM).filter(ClientsORM.NickName == nickname).first()
    client_password_check = session.query(ClientsORM).filter(ClientsORM.Password == hashed_password).first()
    if client_nickname_check and client_password_check:
        print("Вы успешно вошли в систему!")
        after_login_success(nickname)
    else:
        print("Неверное имя пользователя или пароль.")
