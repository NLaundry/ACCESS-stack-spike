from typing import Optional

from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from prisma import Prisma
from prisma.models import Post

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class ItemRequest(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int


async def frank(post: Post) -> Post:
    db = Prisma()
    await db.connect()
    bob = await db.post.create(
        {
            "title": "My first post",
            "published": False,
            "desc": "This is a description of the post.",
        }
    )
    print(bob)
    return bob


@app.get("/bob")
async def bob() -> Post:
    db = Prisma()
    await db.connect()
    bob = await db.post.create(
        {
            "title": "My first post",
            "published": False,
            "desc": "This is a description of the post.",
        }
    )
    print(bob)
    return bob


@app.post("/items/")
async def create_item(item: ItemRequest):
    #
    # Here, you can use `item` as the python object
    #
    return item


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# Asynchronous mode
@app.get("/models/{model_id}")
async def read_model(model_id: int, level: Optional[str] = None):
    return {"model_id": model_id, "level": level}
