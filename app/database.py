from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from .config import settings
# Creates SQLAlchemy engine and SessionLocal class for DB sessions

# Build a safe, explicit URL (escapes special chars and adds SSL when needed)
sslmode = "require"  # Railway Postgres needs SSL

db_url = URL.create(
    "postgresql+psycopg2",                   # explicit driver
    username=str(settings.database_username),
    password=str(settings.database_password),
    host=str(settings.database_hostname),
    port=int(settings.database_port),
    database=str(settings.database_name),
    query={"sslmode": settings.database_sslmode},   # <--- toggle here
)
engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get DB session for FastAPI endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()