from src.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String,Boolean
from sqlalchemy.sql.schema import ForeignKey
from src.connection import user
from sqlalchemy.orm import relationship

class article2 (Base):
    __tablename__='article'
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer,ForeignKey('user.id'))
    user= relationship("user",back_populates='items')
