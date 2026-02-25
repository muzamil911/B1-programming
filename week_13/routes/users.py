from fastapi import APIRouter, HTTPException, Query
from schema import User, UserCreate
import json
import os

router = APIRouter()
DB_FILE = "users.txt"

# --- Helper Functions (Persistence Logic) ---
def read_users():
    if not os.path.exists(DB_FILE) or os.stat(DB_FILE).st_size == 0:
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=4)

def get_next_id(users):
    if not users: return 1
    return max(user['id'] for user in users) + 1

# --- Endpoints ---

@router.post("/", response_model=User)
def create_user(user_in: UserCreate):
    users = read_users()
    new_user_data = user_in.model_dump() # Convert Pydantic to Dict
    new_user_data["id"] = get_next_id(users)
    
    # We remove the password before saving/returning for safety
    password = new_user_data.pop("password") 
    
    users.append(new_user_data)
    write_users(users)
    return new_user_data

@router.get("/")
def get_all_users():
    return read_users()

# IMPORTANT: Define /search BEFORE /{id}
@router.get("/search")
def search_users(q: str = Query(..., description="Search by username")):
    users = read_users()
    results = [u for u in users if q.lower() in u['username'].lower()]
    return results

@router.get("/{id}", response_model=User)
def get_user_by_id(id: int):
    users = read_users()
    user = next((u for u in users if u["id"] == id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{id}")
def delete_user(id: int):
    users = read_users()
    initial_length = len(users)
    users = [u for u in users if u["id"] != id]
    
    if len(users) == initial_length:
        raise HTTPException(status_code=404, detail="User not found")
    
    write_users(users)
    return {"message": f"User {id} deleted successfully"}