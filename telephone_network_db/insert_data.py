from telephone_network_connection_to_db import connection, execute_query
import hashlib
import sqlite3


def insert_data_into_clients_table(nickname, password):
    connection = sqlite3.connect('telephone_network_db.sqlite')
    cursor = connection.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO Clients(NickName, Password) "
                   "VALUES (?, ?)",
                   (nickname, hashed_password))
    connection.commit()
    connection.close()
    print("Пользователь зарегистрирован успешно!")


insert_data_into_clients_table('nikita', 'nikita')
insert_data_into_clients_table('test', 'test')

insert_client_info = """
INSERT INTO
    Client_Info (FirstName, SecondName, Patronymic, Address, Email)
VALUES
('Никита', 'Пупанов', 'Сергеевич', 'ЕвленИпподромнаятьево', 'nikita@mail.ru'),
('Тест', 'Тест', 'Тест', 'Тест', 'test@mail.ru')
"""

insert_client_devices = """
INSERT INTO
Client_Devices (ClientID, DeviceType, PhoneNumber, SubscriptionPlan, Balance)
VALUES
(1, 'Домашний телефон', '666-666', 'Базовый домашний тариф', 490.50),
(1, 'Мобильный телефон', '+79517513766', 'Базовый мобильный тариф', 300),
(2, 'Мобильный телефон', '+79532384458', 'Базовый мобильный тариф', 300)
"""

insert_number_call = """
INSERT INTO
Number_Call (DeviceID, Duration)
VALUES
(1, 3),
(1, 2),
(1, 10),
(2, 8),
(2, 3),
(3, 2),
(3, 14),
(3, 7),
(3, 2)
"""

execute_query(connection, insert_client_info)
execute_query(connection, insert_client_devices)
execute_query(connection, insert_number_call)
