from passlib.context import CryptContext

# set up password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# use .hash to hash password
def hash(password: str):
    return pwd_context.hash(password)

# Verfy plain password with hashed password
def verify(plan_password: str, hashed_password: str):
    return pwd_context.verify(plan_password, hashed_password)