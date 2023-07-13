from fastapi import APIRouter, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from src.database import get_db
from fastapi.param_functions import Depends
from src.connection import user
from src.connection.hash import Hash
from src.authorization import oauth2

router = APIRouter(tags=['authentication'])

@router.post('/token')
def get_token(request:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    users = db.query(user.user).filter(user.user.name == request.username).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail ="invalid credentials")
    if not Hash.verify(users.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="incorrect password")
    
    access_token= oauth2.create_access_token(data={'sub':users.name})

    return {
        'access_token':access_token,
        'token_type': 'bearer',
        'user_id':users.id,
        'user_name':users.name}

