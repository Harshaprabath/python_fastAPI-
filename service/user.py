from http.client import HTTPException

from db import connection
from model.user import UserModel


def save(user: UserModel):
    if user.id == 0 or user.id is None:
        dbc = connection.connection()
        sql = 'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)'
        dbc.execute(sql, (user.name, user.email, user.password))
        dbc.connection.commit()
        dbc.close()
        return {"message": "success saved"}
    else:
        dbc = connection.connection()
        sql = "UPDATE users SET name=%s, email=%s, password=%s WHERE id=%s"
        dbc.execute(sql, (user.name, user.email, user.password, user.id))
        dbc.connection.commit()
        dbc.close()
        return {"status": "User updated successfully"}


def getAll():
    dbc = connection.connection()
    try:
        sql = 'SELECT * FROM users'
        dbc.execute(sql)

        users = dbc.fetchall()

        return users
    finally:
        dbc.close()


def delete(user_id: int):
    dbc = connection.connection()
    try:
        sql = 'DELETE FROM users WHERE id=%s'
        dbc.execute(sql, (user_id,))

        if dbc.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")

        dbc.connection.commit()
    finally:
        dbc.close()


def getuser(user_id: int):
    dbc = connection.connection()

    # Execute the SELECT query
    dbc.execute(f"SELECT * FROM users WHERE id = {user_id}")

    # Fetch the result
    user = dbc.fetchall()

    # Close the cursor and connection
    dbc.close()
    dbc.close()

    # Return the result
    return user

