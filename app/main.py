from fastapi import FastAPI
from . import models
from .database import engine
from .config import settings
# import routers
from .routers import post, user, auth, vote

# Creates DB tables
models.Base.metadata.create_all(bind=engine)

# Create a FastAPI instance
app = FastAPI()

# Contains a raw psycopg2 connection helper, used for direct SQL testing
# def connect_to_db():
#     while True:
#         try:
#             connection = psycopg2.connect(
#                 host="localhost",
#                 database="fastapi",
#                 user="kylepark",
#                 password="Place3Catch334*",
#                 cursor_factory=RealDictCursor
#             )
#             cursor = connection.cursor()
#             print("Database connection was successful!")
#             return connection, cursor
#         except Exception as error:
#             print("Connecting to database failed")
#             print("Error:", error)
#             time.sleep(2)

# Registers routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# Path operation for the root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}


