from db import connection

dbc = connection.connection()
def user_seeder():
    def add_user(name, email, password):
        # Create a cursor object

        # Insert a user into the database
        sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        dbc.execute(sql, (name, email, password))

        # Commit the changes
        dbc.connection.commit()

    users = [
        ('JaneDoe', 'janedoe@example.com', 'password'),
        ('BobSmith', 'bobsmith@example.com', 'password'),
        ('AliceJones', 'alicejones@example.com', 'password'),
        ('TomWilliams', 'tomwilliams@example.com', 'password')
    ]

    for user in users:
        add_user(*user)

    dbc.close()



