from telephone_network_db.alchemy.database import engine, session_factory
from telephone_network_db.alchemy.models import ClientsORM, ClientInfoORM, ClientDevicesORM, NumberCallORM
import hashlib

session = session_factory()

# пример ORM-запроса на поиск с фильтром
# Clients = session.query(ClientsORM).filter(ClientsORM.NickName == 'nikita').all()
# for client in Clients:
#     print(client.NickName, client.Password)


# пример ORM-запроса на добавление данных в таблицу БД
# password = 'test'
# password = hashlib.sha256(password.encode()).hexdigest()
# test_user = ClientsORM(NickName='test', Password=password)
# session.add(test_user)
# session.commit()


# пример ORM-запроса на объединение таблиц по ID
# clients_join = session.query(ClientsORM, ClientInfoORM).join(ClientInfoORM, ClientsORM.ID == ClientInfoORM.ClientID).all()
# for client, client_info in clients_join:
#     print(client.NickName, client_info.FirstName)


# пример ORM-запроса на удаление клиента по никнейму
# delete_user = session.query(ClientsORM).filter(ClientsORM.NickName == 'test').first()
# if delete_user:
#     session.delete(delete_user)
#     session.commit()


# пример ORM-запроса на изменение никнейма клиента
# update_user = session.query(ClientsORM).filter(ClientsORM.NickName == 'nikita').first()
# if update_user:
#     update_user.NickName = 'test'
#     session.commit()


