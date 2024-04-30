from telephone_network_connection_to_db import create_connection
from sqlite3 import Error

connection = create_connection(
    "C:\\Users\\Никита\\PycharmProjects\\telephone_network_4var\\telephone_network_db\\telephone_network_db.sqlite")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


select_from_number_call = """
SELECT * FROM Number_Call WHERE DeviceID = 1
"""

number_calls = execute_read_query(connection, select_from_number_call)

for number_call in number_calls:
    print(number_call)
