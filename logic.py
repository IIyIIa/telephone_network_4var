import hashlib
import sqlite3
import sys
from telephone_network_db.alchemy.database import session_factory
from telephone_network_db.alchemy.orm import ClientsORM, ClientInfoORM, ClientDevicesORM


def after_login_success(nickname):
    session = session_factory()
    clients = session.query(ClientsORM).filter(ClientsORM.NickName == nickname).all()
    client_info = session.query(ClientsORM, ClientInfoORM).join(ClientInfoORM, ClientsORM.ID == ClientInfoORM.ClientID).all()
    client_devices = session.query(ClientsORM, ClientDevicesORM).join(ClientDevicesORM, ClientsORM.ID == ClientDevicesORM.ClientID).all()
    for client in clients:
        print('Контактные данные:')
        print(f"Никнейм: {client.NickName}")
        for client_info_tuple in client_info:
            client_orm, client_info_orm = client_info_tuple
            if client_orm.ID == client.ID:
                print(f"Имя: {client_info_orm.FirstName} \nФамилия: {client_info_orm.SecondName} \nОтчество: "
                      f"{client_info_orm.Patronymic} \nАдрес: {client_info_orm.Address} \nПочта: {client_info_orm.Email}")
        for client_device in client_devices:
            client_orm, client_device_orm = client_device
            if client_orm.ID == client.ID:
                print(f"Номер телефона: {client_device_orm.PhoneNumber}, баланс = {client_device_orm.Balance} рублей"
                      f"\nУ вас подключен абонентский план: {client_device_orm.SubscriptionPlan}")
    session.close()


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
        print('---------------------------')
        print("Вы успешно вошли в систему!")
        after_login_success(nickname)
    else:
        print("Неверное имя пользователя или пароль.")
