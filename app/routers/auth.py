from fastapi import APIRouter, Depends, HTTPException, status, Response 
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import database, schemas, models, utils, oauth2

# Login route that validates credentials and returns access token
# Depends on utils/oauth2 to create/verify JWT tokens
# Provides current_user dependency in protected routes

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schemas.Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    # user doesn't exist
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    # password is incorrect
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    # Create token
    access_token = oauth2.create_access_token(data={"user_id": str(user.id)})

    # Return Token
    return {"access_token": access_token, "token_type": "bearer"}