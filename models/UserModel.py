from database.db_base import Base
from sqlalchemy import Column, Integer, String, Boolean


class Users(Base):
    id=Column(Integer,primary_key=True, nullable=False)
    name=Column(String(20), nullable=False)
    email=Column(String(20), nullable=False, unique=True)
    password= Column(String(100), nullable=False)
    mobile_num= Column(Integer, nullable=False)
    status= Column(Boolean,default=False)
    is_activated = Column(Boolean, default=False)
    reset_token = Column(String(500), nullable=True)
