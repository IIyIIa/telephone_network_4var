from telephone_network_db import connection, execute_query

create_clients_table = """
CREATE TABLE IF NOT EXISTS Clients (
        ClientID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT,
        LastName TEXT,
        MiddleName TEXT,
        Address TEXT,
        Phone TEXT,
        Email TEXT
    )
"""

create_devices_clients_table = """
CREATE TABLE IF NOT EXISTS Client_devices (
        DeviceID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER NOT NULL,
        DeviceName TEXT,
        DeviceType TEXT,
        FOREIGN KEY (UserID) REFERENCES Clients (ClientID)
    )
"""

create_clients = """
INSERT INTO 
    Clients (FirstName, LastName, MiddleName, Address, Phone, Email)
VALUES
('Никита', 'Пупанов', 'Сергеевич', 'адрес', 'телефон', 'nicitapupanov@yandex.ru'),
('Test', 'Test', 'Test', 'адрес', 'телефон', 'test@yandex.ru')
"""

create_client_devices = """
INSERT INTO 
    Client_devices (UserID, DeviceName, DeviceType)
VALUES
('1', 'Samsung M32', 'Мобильный телефон'),
('1', 'Home-Phone-3000', 'Домашний телефон')
"""

execute_query(connection, create_clients_table)
execute_query(connection, create_devices_clients_table)

