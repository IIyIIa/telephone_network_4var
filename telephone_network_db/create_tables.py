from telephone_network_connection_to_db import connection, execute_query

create_clients_table = """
CREATE TABLE IF NOT EXISTS Clients (
        ID INTEGER PRIMARY KEY,
        NickName TEXT NOT NULL UNIQUE,
        Password TEXT NOT NULL
    )
"""

create_client_info_table = """
CREATE TABLE IF NOT EXISTS Client_Info (
        ClientID INTEGER NOT NULL PRIMARY KEY UNIQUE,
        FirstName TEXT NOT NULL,
        SecondName TEXT NOT NULL,
        Patronymic TEXT NOT NULL,
        Address TEXT NOT NULL,
        Email TEXT NOT NULL UNIQUE,
        FOREIGN KEY (ClientID) REFERENCES Clients (ID)
    )
"""

create_devices_client_table = """
CREATE TABLE IF NOT EXISTS Client_Devices (
        ID INTEGER PRIMARY KEY,
        ClientID INTEGER NOT NULL,
        DeviceType TEXT NOT NULL,
        PhoneNumber TEXT NOT NULL UNIQUE,
        SubscriptionPlan TEXT NOT NULL,
        Balance REAL,
        FOREIGN KEY (ClientID) REFERENCES Clients (ID)
    )
"""

create_number_call_table = """
CREATE TABLE IF NOT EXISTS Number_Call (
        ID INTEGER PRIMARY KEY,
        DeviceID INTEGER NOT NULL,
        Duration INTEGER NOT NULL,
        FOREIGN KEY (DeviceID) REFERENCES Client_devices (ID)
    )
"""

execute_query(connection, create_clients_table)
execute_query(connection, create_client_info_table)
execute_query(connection, create_devices_client_table)
execute_query(connection, create_number_call_table)

