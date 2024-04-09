from telephone_network_db import connection, execute_query

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

execute_query(connection, create_clients)
execute_query(connection, create_client_devices)
