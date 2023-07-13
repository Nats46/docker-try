from fastapi import APIRouter,Depends
from src.connection.schema import UserBase,UserDisplay
from sqlalchemy.orm import Session
from src.database import get_db
from src.connection import db_user
from typing import List

router = APIRouter(prefix='/user',tags=['user'])

@router.post('/', response_model=UserDisplay)
def create_user(request:UserBase,db:Session=Depends(get_db)):
    return db_user.create_user(db,request)


@router.get('/getall',response_model=List[UserDisplay])
def get_all_user(db:Session=Depends(get_db)):
    return db_user.get_all_user(db)

@router.get('/get/{id}',response_model=UserDisplay)
def get_user_id(id:int,db:Session=Depends(get_db)):
    return db_user.get_user_id(db,id)

@router.put('/update/{id}')
def update_user(id:int,request:UserBase,db:Session=Depends(get_db)):
    return db_user.update_user(db,id,request)

@router.delete('/delete/{id}')
def delete_user(id:int,db:Session=Depends(get_db)):
    return db_user.delete_user(db,id)