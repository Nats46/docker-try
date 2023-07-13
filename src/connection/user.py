from src.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship


class user (Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship("article2",back_populates='user')