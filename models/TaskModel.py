from sqlalchemy.orm import relationship
from database.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from . import UserModel
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer,primary_key = True, nullable = False)
    title = Column(String(100), nullable = False)
    description = Column(String(500), nullable = False)
    is_complete = Column(Boolean, default = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    created_by = Column(Integer, ForeignKey('users.id') ,nullable = False)

    # created_by = relationship(UserModel.Users)