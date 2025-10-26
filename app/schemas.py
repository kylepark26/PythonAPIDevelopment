from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime

# Comes from Pydantic library, schema to validate data
class PostBase(BaseModel):
    title: str
    content: str 
    published: bool = True 

class PostCreate(PostBase):
    pass 


class PostResponse(PostBase):
    id: int
    created_at: datetime

    class Config:
         model_config = ConfigDict(from_attributes=True)

# Schema For User
class UserCreate(BaseModel):
    email: EmailStr
    password: str 

# Schema for User Resposne
# Schema for Fetch User Response
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        model_config = ConfigDict(from_attributes=True)

# Schema for Fetch User Response