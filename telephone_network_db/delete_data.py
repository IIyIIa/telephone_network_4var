from telephone_network_connection_to_db import connection, execute_query

delete_client = """
DELETE FROM Clients
WHERE ID = 2
"""

execute_query(connection, delete_client)
