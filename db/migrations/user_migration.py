from db import connection

dbc = connection.connection()
def user_migration():
    dbc.execute("CREATE TABLE users "
                "(id INT AUTO_INCREMENT PRIMARY KEY,"
                "name VARCHAR(255), "
                "email VARCHAR(255),"
                "password VARCHAR(255))")

    dbc.close()