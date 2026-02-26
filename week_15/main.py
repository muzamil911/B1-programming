from fastapi import FastAPI
from routes import users  # This connects to routes/users.py

app = FastAPI(
    title="User Management API - Week 14",
    description="Refactored API using the UserStore Class",
    version="2.0.0"
)

# Connect the refactored router
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def health_check():
    return {
        "status": "healthy", 
        "message": "API is running with UserStore class logic"
    }

@app.get("/health")
def detailed_health():
    return {"status": "UP", "persistence": "JSON File via UserStore"}