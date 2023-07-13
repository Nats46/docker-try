from fastapi import APIRouter,status,exceptions,Response,Query,Body,Path
from typing import Optional,List
from enum import Enum
from passlib.context import CryptContext
from pydantic import BaseModel

blog=APIRouter(tags=['blog'],prefix="/blog")


@blog.get('/all', tags=['blog'], summary='retrieve all blog',description='this API call similates fetching all blog')
def get_all(page=1, page_size:Optional[int]=None):
    return{'Message':'all {page_size} blogs on page{page}'}

# @app.get('/blog/all', tags=['blog'])
# def get_all(page: int = 1, page_size: Optional[int] = None):
#     return {'Message': f'all {page_size} blogs on page {page}'}

class blog_type(str,Enum):
    short :'short'
    story:'story'
    howto:'howto'

@blog.get('/type/{type}', tags=['blog'])
def get_type(type : blog_type):
    return {'Message':'blog type {type}'}

@blog.get('/{id}/comments/{comment_id}',tags=['blog','comment'])
def get(id:int,comment_id:int,valid:bool=True, username:Optional[str]=None):
    """
    Simulates retrieving a comment of a blog        
    - **id** is a mandatory path parameter
    - **comment_id** is a mandatory path parameter
    - **valid** is a mandatory query parameter
    - **username** is a mandatory query parameter
    """
    return{'Message':'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}


@blog.get('/{id}',status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id:int, respone:Response):
    if id>5:
        respone.status_code=status.HTTP_404_NOT_FOUND
        return {'error':'id not found'}
    else:
        respone.status_code=status.HTTP_200_OK  
        return {'Message':'Bog with id {id}'}

pwd_cxt=CryptContext(schemes='bcrypt',deprecated='auto')

class hash():
    def bcrypt(password:str):
        return pwd_cxt.hash(password)
    
    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(hashed_password,plain_password)

#request body
class Image(BaseModel):
    url:str
    alias:str

class BlogModel(BaseModel):
    title:str
    content:str
    no_comment:int
    published: Optional[bool]
    tags:List[str]={}
    metadata:dict[str,str]={'key1':'val1'}
    image:Optional[Image]=None

@blog.post('/new')
def create_blog(blog:BlogModel):
    return {'data':blog}

@blog.post('/new/{id}')
def create_blog(blog:BlogModel,id:int,version:int=1):
    return{
        'id':id,
        'data':blog,
        'version':version 
    }

@blog.post('/new/{id}/comment')
def create_comment(blog:BlogModel,id:int,comment_title:int=Query(None,title= 'id of the comment',description='some description for comment id', alias='CommentID', deprecated=True),content:str=Body(...,min_length=10,regex='^[a-z\s]*$'),content2:str=Body(...,max_length=10,regex='^[A-Z\s]*$'),v:Optional[List[str]]=Query(['1.0','1.1','1.2']),comment_id:int=Path(..., gt=1,le=10)):
    return {
        'blog':blog,
        'id':id,
        'comment_title':comment_title,
        'content':content,
        'content2':content2,
        'version':v,
        'comment_id':comment_id
    }

