from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from schemas import UserCreate, UserUpdate

from database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "FastAPI MySQL Learning Project"}


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM users"))
    return result.mappings().all()

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    query = text("SELECT * FROM users WHERE id = :user_id")
    result = db.execute(query, {"user_id": user_id})

    user = result.mappings().first()
    if user is None:
        return {"message": "User not found"}
    return user
    


@app.post("/users", status_code=201)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    check_query = text("""
        SELECT id 
        FROM users
        WHERE email = :email
    """)
    existing_user = db.execute(check_query,
         {"email": user.email}).first()
    if existing_user:
        raise HTTPException(
            status_code=400, detail="Email already exists"
        )
    insert_query = text("""
        INSERT INTO users (name, email)
        VALUES (:name, :email)
        """)
    
    db.execute(
        insert_query,
        {
            "name": user.name,
            "email": user.email
        }
    )

    db.commit()

    return {
        "message": "User created successfully",
        "name": user.name,
        "email": user.email
    }

@app.put("/users/{user_id}")
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    query = text("""
        UPDATE users
        SET name = :name, email = :email
        WHERE id = :user_id""")
    result = db.execute(
        query,{
            "user_id": user_id,
            "name": user.name,
            "email": user.email
        }
    )

    db.commit()

    if result.rowcount == 0:
        return {"message": "user not found"}
    return {
        "message": "user updated successfully",
        "id": user_id,
        "name": user.name,
        "email": user.email
        
    }
    

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    query = text("DELETE FROM users WHERE id = :user_id")
    result = db.execute(query, {"user_id": user_id})

    db.commit()

    if result.rowcount == 0:
        return {"message": "user not found"}
    return {"message": "user deleted successfully", "id": user_id}