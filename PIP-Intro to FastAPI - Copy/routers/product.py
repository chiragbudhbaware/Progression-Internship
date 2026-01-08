from fastapi import APIRouter

from typing import Optional

 

router = APIRouter(

    prefix="/products",

     tags=["products"]

)

 

@router.get("")

def get_products(

    category : Optional[str] = None,

    page: int = 1

):

    return {

        "message": f"Fetching products in {category} on page {page}"

    }




