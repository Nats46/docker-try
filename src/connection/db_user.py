from sqlalchemy.orm.session import Session
from src.connection.schema import UserBase
from src.connection.user import user
from src.connection.hash import Hash
from fastapi import HTTPException,status

def create_user(db:Session, request:UserBase):
    new_user = user(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_user(db:Session):
    return db.query(user).all()

def get_user_id(db:Session, id:int):
    player = db.query(user).filter(user.id==id).first()
    if not player: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return player

def get_user_name(db:Session, name:str):
    player =  db.query(user).filter(user.name==name).first()
    if not player: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return player

def update_user(db:Session, id:int, request:UserBase):
    user2= db.query(user).filter(user.id==id)
    user2.update({
        user.name: request.name,
        user.email:request.email,
        user.password:Hash.bcrypt(request.password)
    })
    db.commit()
    return 'ok'

def delete_user(db:Session,id:int):
    user2=db.query(user).filter(user.id==id).first()
    db.delete(user2)
    db.commit()
    return 'ok'
