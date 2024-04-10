from telephone_network_db import connection, execute_query

create_clients_table = """
CREATE TABLE IF NOT EXISTS Clients (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NickName TEXT NOT NULL,
        PhoneNumber TEXT NOT NULL,
        Password TEXT NOT NULL
    )
"""

create_devices_client_table = """
CREATE TABLE IF NOT EXISTS Client_devices (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ClientID INTEGER NOT NULL,
        DeviceType TEXT NOT NULL, # домашний или мобильный
        SubscriptionPlan TEXT NOT NULL,
        Balance TEXT NOT NULL,
        FOREIGN KEY (ClientID) REFERENCES Clients (ID)
    )
"""

create_devices_clients_table = """
CREATE TABLE IF NOT EXISTS Number_call (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DeviceID INTEGER NOT NULL,
        PhoneNumber TEXT NOT NULL,
        Duration INTEGER NOT NULL,
        FOREIGN KEY (DeviceID) REFERENCES Client_devices (ID),
        FOREIGN KEY (PhoneNumber) REFERENCES Clients (PhoneNumber)
    )
"""

execute_query(connection, create_clients_table)
execute_query(connection, create_devices_client_table)
