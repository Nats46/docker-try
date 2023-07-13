from fastapi import APIRouter,Depends
from src.connection.schema import articleBase,articleDisplay
from sqlalchemy.orm import Session
from src.database import get_db
from src.connection import db_article
from typing import List
from src.authorization.oauth2 import oauth2_scheme
from src.authorization.oauth2 import get_current_user
from src.connection.schema import UserBase

router = APIRouter(prefix='/article',tags=['article'])

@router.post('/create',response_model=articleDisplay)
def create_article(request:articleBase,db:Session=Depends(get_db)):
    return db_article.create_article(db,request)

@router.get('/get/{id}') #,response_model=articleDisplay)
def get_article(id:int,db:Session=Depends(get_db),current_user:UserBase =Depends(get_current_user)):
    return {
        'data':db_article.get_article(db,id),
        'current_user':current_user}

