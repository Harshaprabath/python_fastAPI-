from fastapi import Path, APIRouter

from model.user import UserModel
from service.user import save, getAll, delete, getuser

router = APIRouter()


@router.get("/user/getall")
def get_users():
    return getAll()


@router.post("/user/save")
def create_user(user: UserModel):
    return save(user)


@router.delete("/user/delete/{user_id}")
def delete_user(user_id: int = Path(..., title="The ID of the user to delete")):
    return delete(user_id)


@router.get("/user/getuser/{user_id}")
def get_user(user_id: int):
    return getuser(user_id)


@router.put("/user/edit")
def update_user(user: UserModel):
    return save(user)
