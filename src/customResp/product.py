from fastapi import APIRouter,Depends,Header,Cookie,Form
from src.connection.schema import articleBase,articleDisplay
from sqlalchemy.orm import Session
from src.database import get_db
from src.connection import db_article
from typing import List
from fastapi.responses import Response, HTMLResponse,PlainTextResponse
from typing import Optional

router = APIRouter(prefix='/product',tags=['product'])

product=['watch','camera','phone']

#form data
@router.post('/new')
def create_product(name:str=Form(...)):
    product.append(name)
    return product

#Responses
@router.get('/all')
def get_all():
    data=" ".join(product)
    responses=Response(content=data,media_type="text/plain")
    responses.set_cookie(key="test_cookie",value="test_cookie_value")
    return responses

@router.get('/get_products/{id}',responses={200:{"content":{"text/html":{"<div>product</div>"}},"description":"returns HTML for object"},404:{"content":{"text/plain":{"product not available"}},"description":"a clear text error message"}})
def get_product(id:int):
    if id>len(product):
        out = "product not available"
        return PlainTextResponse(status_code=404,content=out,media_type="text/plain")
    else:
        products = product[id]
        out=f"""
        <head>
            <style>
            products{{
            widt:500px;
            height:30px;
            border:2px insert green;
            text-align:center;
            }}
            </style>
        </head>
        <div class ="products">{products}</div>
        """
        return HTMLResponse(content=out, media_type="text/html")


#header
@router.get('/header')
def get_product(response:Response,custom_header:Optional[str]=Header(None), test_cookie:Optional[str]=Cookie(None)):
    return {'data':product,'custom_header':custom_header,'cookie':test_cookie}

@router.get('/headermany')
def get_product(response:Response,custom_header:Optional[List]=Header(None)):
    response.headers['custom_response_header']=", ".join(custom_header)
    return product





