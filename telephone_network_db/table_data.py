from telephone_network_db import connection, execute_query

create_clients = """
INSERT INTO 
    Clients (NickName, PhoneNumber, Password)
VALUES
(),
()
"""

create_client_devices = """
INSERT INTO 
    Client_devices (ClientID, DeviceType)
VALUES
(),
()
"""

execute_query(connection, create_clients)
execute_query(connection, create_client_devices)
