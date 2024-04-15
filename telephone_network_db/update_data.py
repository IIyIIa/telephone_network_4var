from telephone_network_connection_to_db import connection, execute_query

update_clients = """
UPDATE
Clients
SET
Nickname = 'n1gida'
WHERE ID = 1
"""

execute_query(connection, update_clients)