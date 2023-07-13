from pydantic import BaseModel
from typing import List

class article(BaseModel):
    title:str
    content:str
    published:bool
    class Config():
        orm_mode = True

class UserBase(BaseModel):
    name:str
    email:str
    password:str

class UserDisplay(BaseModel):
    name:str
    email:str
    items:List[article]=[]
    class Config():
        orm_mode = True



class articleBase(BaseModel):
    title:str
    content:str
    published:bool
    creator_id:int

class User(BaseModel):
    id:int
    name:str
    class Config():
        orm_mode = True

class articleDisplay(BaseModel):
    title:str
    content:str
    published:bool
    user:User
    class Config():
        orm_mode = True