from fastapi import FastAPI
from .database import engine
from . import models
from .routers import post,user,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# try:
#     conn = psycopg2.connect(host='localhost',database='fastapi',port=5433,user='postgres',password=19021991,cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("DB connection was successful")
# except Exception as e:
#     print("Connection failed")
#     print("Error: ",e)

# my_posts=[{"title":"title fo post 1","content":"content of post 1","id":1},
#             {"title":"favourite foods","content":"I like pizza","id":2}]




# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p['id'] == id:
#             return id


@app.get("/")
def root():
    return {"message": "Hello World"}



