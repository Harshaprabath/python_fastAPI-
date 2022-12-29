from fastapi import HTTPException, Path, APIRouter
from pydantic import BaseModel

from db import connection

router = APIRouter()

class UpdateUserModel(BaseModel):
    id: int
    name: str
    email: str

@router .get("/getallusers")
def get_users():
    dbc = connection.connection()
    try:
        sql = 'SELECT * FROM users'
        dbc.execute(sql)

        users = dbc.fetchall()

        return users
    finally:
        dbc.close()

@router .post("/users")
def create_user(name: str, email: str, password: str):
    dbc = connection.connection()
    try:
        sql = 'INSERT INTO `users` (`name`, `email`, `password`) VALUES (%s, %s, %s)'
        dbc.execute(sql, (name, email, password))

        dbc.connection.commit()

        return {'id': dbc.lastrowid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:

        dbc.close()

@router .delete("/users/{user_id}")
def delete_user(user_id: int = Path(..., title="The ID of the user to delete")):
    dbc = connection.connection()
    try:
        sql = 'DELETE FROM users WHERE id=%s'
        dbc.execute(sql, (user_id,))

        if dbc.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")

        dbc.connection.commit()
    finally:
        dbc.close()

@router .get("/getuser/{user_id}")
def get_user(user_id: int):
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

@router.put("/user/{user_id}")
def update_user(user_id: int, new_username: str, new_email: str,new_password: str):
    dbc = connection.connection()

    sql = "UPDATE users SET name=%s, email=%s, password=%s WHERE id=%s"
    dbc.execute(sql, (new_username, new_email, new_password, user_id))
    dbc.connection.commit()
    return {"message": "User updated successfully"}