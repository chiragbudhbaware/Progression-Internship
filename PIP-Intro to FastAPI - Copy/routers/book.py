from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel

 

router = APIRouter(

    prefix="/book",

    tags=["books"]

)

class BookModel(BaseModel):
    title:str
    author:str
    price:float
    in_stock:Optional[bool] = True


@router.post("/new")

def create_book(book: BookModel):
    return {
        "message": "Book Added successfully",
        "author":book.author,
        "title":book.title,
        
    }