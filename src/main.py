from fastapi import FastAPI
from src.connection import user
from src.database import engine
from src.connection import router,articlerouter
from src.blogdesc import blog
from src.customResp import product
from src.authorization import uthentication
from src.files import file
from fastapi.staticfiles import StaticFiles

import src.database
app = FastAPI()
app.mount('/files',StaticFiles(directory="files/filestore"),name=('files'))

user.Base.metadata.create_all(engine)
app.include_router(uthentication.router)
app.include_router(router.router)
app.include_router(blog.blog)
app.include_router(articlerouter.router)
app.include_router(product.router)
app.include_router(file.router)

