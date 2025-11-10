from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime
from typing import Optional

# Pydantic models used for request validation and response serialization.

# Comes from Pydantic library, schema to validate data
class PostBase(BaseModel):
    title: str
    content: str 
    published: bool = True 

class PostCreate(PostBase):
    pass 

# Schema for User Resposne
# Schema for Fetch User Response
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        model_config = ConfigDict(from_attributes=True)

# Schema for User Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: 'UserOut'

    class Config:
         model_config = ConfigDict(from_attributes=True)

# Schema For User
class UserCreate(BaseModel):
    email: EmailStr
    password: str 

# Schema for Token
class Token(BaseModel):
    access_token: str
    token_type: str

# Schema for Token Data
class TokenData(BaseModel):
    id: Optional[str] = None