from fastapi import APIRouter, HTTPException
from schema import User, UserCreate
from user_store import UserStore

router = APIRouter()
# 1. Initialize Store
store = UserStore("users.txt")

@router.get("/")
def get_users():
    # 2. Use store.load()
    return store.load()

@router.post("/", response_model=User)
def create_user(user_in: UserCreate):
    users = store.load()
    
    # Logic for new user
    new_user_dict = user_in.model_dump()
    new_id = max([u["id"] for u in users], default=0) + 1
    new_user_dict["id"] = new_id
    
    # Remove password for persistence
    new_user_dict.pop("password", None)
    
    users.append(new_user_dict)
    # 3. Use store.save()
    store.save(users)
    return new_user_dict

@router.get("/{id}", response_model=User)
def get_user_by_id(id: int):
    user = store.find_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 3. Extension Challenge: PUT and DELETE Endpoints
@router.put("/{id}")
def update_existing_user(id: int, user_update: UserCreate):
    # We exclude the password from the update for this lab's scope
    data = user_update.model_dump(exclude={"password"})
    if store.update_user(id, data):
        return {"message": "User updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{id}")
def delete_existing_user(id: int):
    if store.delete_user(id):
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")