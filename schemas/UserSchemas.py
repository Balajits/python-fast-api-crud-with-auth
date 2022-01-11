from typing import Optional
from pydantic import BaseModel, EmailStr



class User(BaseModel):
    name: str
    email: EmailStr
    password:str
    mobile_num:int

    class Config:
        orm_mode = True



class GetUser(User):
    id: int



class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None