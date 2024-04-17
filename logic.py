import hashlib
import sqlite3
from telephone_network_db.alchemy.database import session_factory
from telephone_network_db.alchemy.orm import ClientsORM, ClientInfoORM, ClientDevicesORM, NumberCallORM
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def calculate_cost(self, duration):
        pass


class BasicHomeStrategy(Strategy):
    def calculate_cost(self, duration):
        return duration * 2


class PremiumHomeStrategy(Strategy):
    def calculate_cost(self, duration):
        return duration * 1.5


class BasicMobileStrategy(Strategy):
    def calculate_cost(self, duration):
        return duration * 1.2


class PremiumMobileStrategy(Strategy):
    def calculate_cost(self, duration):
        return duration * 1.05


def after_login_success(nickname):
    session = session_factory()
    clients = session.query(ClientsORM).filter(ClientsORM.NickName == nickname).all()
    client_info = session.query(ClientsORM, ClientInfoORM).join(ClientInfoORM,
                                                                ClientsORM.ID == ClientInfoORM.ClientID).all()
    client_devices = session.query(ClientsORM, ClientDevicesORM).join(ClientDevicesORM,
                                                                      ClientsORM.ID == ClientDevicesORM.ClientID).all()
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
    while True:
        choice = input("Выберите действие (1 - Совершить звонок, 2 - Выход): ")

        if choice == '1':
            input_number = str(input("Введите номер телефона, с которого хотите совершить звонок: "))
            existing_number = session.query(ClientDevicesORM).filter(
                ClientDevicesORM.PhoneNumber == input_number).first()
            if existing_number:
                duration = int(input("Введите продолжительность звонка в минутах: "))
                tariff_plan = existing_number.SubscriptionPlan
                if tariff_plan == "Базовый домашний тариф":
                    strategy = BasicHomeStrategy()
                elif tariff_plan == "Премиум домашний тариф":
                    strategy = PremiumHomeStrategy()
                elif tariff_plan == "Базовый мобильный тариф":
                    strategy = BasicMobileStrategy()
                elif tariff_plan == "Премиум мобильный тариф":
                    strategy = PremiumMobileStrategy()
                else:
                    print("Не удалось определить тарифный план. Пожалуйста, обратитесь к администратору.")
                    session.close()
                    return
                cost = strategy.calculate_cost(duration)
                if cost > existing_number.Balance:
                    print("Недостаточно средств на балансе для совершения звонка.")
                else:
                    print(f"Звонок будет стоить {cost} рублей.")
                    new_balance = existing_number.Balance - cost
                    existing_number.Balance = new_balance
                    new_call = NumberCallORM(DeviceID=existing_number.ID, Duration=duration)
                    session.add(new_call)
                    session.commit()
                    print(f"Баланс после звонка: {new_balance} рублей.")
            else:
                print("Номер телефона не найден. Пожалуйста, введите существующий номер или выберите другое действие.")
        elif choice == '2':
            session.close()
            return
        else:
            print("Ошибка ввода. Пожалуйста, попробуйте еще раз.")


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
