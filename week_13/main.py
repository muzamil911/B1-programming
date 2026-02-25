from fastapi import FastAPI
from routes import users # This looks into the routes folder

app = FastAPI(
    title="User Management API",
    description="FastAPI backend for managing users",
    version="1.0.0"
)

# Connect the routes from users.py
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def health_check():
    return {"status": "healthy", "message": "API is running"}