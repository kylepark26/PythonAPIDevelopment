from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

# Create a FastAPI instance
app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# global array to store posts
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]


# find post by id helper function
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

# find indexed post
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

# Path operation for the root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}

# post request
@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

# get all posts
@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

# get individual post
@app.get("/posts/{id}")
async def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    return {"post_detail": post}

# deleting
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# updating
@app.put("/posts/{id}")
async def update_post(id: int, post: Post):
    # find index of the post
    index = find_index_post(id)

    # if it doesn't exist, 404 error
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    # convert all data from fronend to dictionary
    post_dict = post.model_dump()
    # we then add the id to the dictionary, since it is not included in the request body
    post_dict['id'] = id
    # so for post at that index, we update it with the new dictionary
    my_posts[index] = post_dict
    # return the updated post
    return {'data': post_dict}