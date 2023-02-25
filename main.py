from typing import Union,List,Optional
from pydantic import BaseModel
from fastapi import FastAPI
from database import SessionLocal
import models

app = FastAPI()

class User(BaseModel):
    user_id:int
    username:Optional[str] = None
    password:Optional[str] = None
    age:int
    email:Optional[str] = None

    class config:
        orm_mode=True


db=SessionLocal()


@app.get("/user",response_model=List[User],status_code=200)
def get_all_user():
    user=db.query(models.User).All()
    return user


            
@app.get("/")
def root():
    return {'Hello':"Python coffee shop"}



@app.get("/users/{user_id}/{q}")
def read_user(user_id: int, q: Union[str, None] = None):
    return {"user_id": user_id, "q": q}



@app.get("/hi")
def hi(name:str , reply:str):
    return {"Hi": name, "reply" :reply}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/login")
def login(user: User):
    return {"echo":user}

