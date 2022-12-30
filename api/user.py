from fastapi import HTTPException, Path, APIRouter

from db import connection
from model.user import UserModel

router = APIRouter()


@router .get("/user/getall")
def get_users():
    dbc = connection.connection()
    try:
        sql = 'SELECT * FROM users'
        dbc.execute(sql)

        users = dbc.fetchall()

        return users
    finally:
        dbc.close()

@router.post("/user/save")
def create_user(user: UserModel):
    dbc = connection.connection()
    sql = 'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)'
    dbc.execute(sql, (user.name, user.email, user.password))
    dbc.connection.commit()
    dbc.close()
    return {"message": "success saved"}

@router .delete("/user/delete/{user_id}")
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

@router.get("/user/getuser/{user_id}")
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

@router.put("/user/edit")
def update_user(user: UserModel):
    dbc = connection.connection()

    sql = "UPDATE users SET name=%s, email=%s, password=%s WHERE id=%s"
    dbc.execute(sql, (user.name, user.email, user.password, user.id))
    dbc.connection.commit()
    dbc.close()
    return {"status": "User updated successfully"}




