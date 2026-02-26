from fastapi import APIRouter, HTTPException
from schema import User, UserCreate
from user_store import UserStore

router = APIRouter()
store = UserStore("users.db")  # Note the change to .db file

@router.get("/")
def get_users():
    return store.load()

@router.post("/", response_model=User)
def create_user(user_in: UserCreate):
    user_dict = user_in.model_dump()
    # Let SQLite handle the ID generation
    new_id = store.save_new_user(user_dict)
    
    # Return the user with their new database ID
    return {**user_dict, "id": new_id}

@router.get("/{id}", response_model=User)
def get_user(id: int):
    user = store.find_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{id}")
def update_user(id: int, user_update: UserCreate):
    if store.update_user(id, user_update.model_dump()):
        return {"message": "User updated in database"}
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{id}")
def delete_user(id: int):
    if store.delete_user(id):
        return {"message": "User deleted from database"}
    raise HTTPException(status_code=404, detail="User not found")