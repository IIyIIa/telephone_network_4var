from telephone_network_db import connection, execute_query

# insert_clients = """
# INSERT INTO
#     Clients (NickName, Password)
# VALUES
# ('IIyIIa', 'niki1967'),
# ('n1gida', 'niki2003')
# """

insert_client_info = """
INSERT INTO 
    Client_Info (FirstName, SecondName, Patronymic, Address, Email)
VALUES
('Никита', 'Пупанов', 'Сергеевич', 'Ипподрмоная', 'pupanov67@mail.ru'),
('Никита', 'Пупанов', 'Сергеевич', 'Ипподрмоная', 'pupanov1967@mail.ru'),
('Никита', 'Пупанов', 'Сергеевич', 'Ипподрмоная', 'pupanovn@mail.ru')
"""

# execute_query(connection, insert_clients)
execute_query(connection, insert_client_info)
