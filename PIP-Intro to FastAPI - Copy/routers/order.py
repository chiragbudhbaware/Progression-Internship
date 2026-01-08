from fastapi import APIRouter

from typing import Optional

 

router = APIRouter(

    prefix="/orders",

    tags=["orders"]

)

 

@router.get("/{order_id}")

def get_order_price(order_id:int, total:float, coupon:Optional[str]=None):

    

    if coupon:

        

        discount_percent = 10

        final_price = total - (total * discount_percent / 100)

        

        return {

            "order_id": order_id,

            "total": total,

            "discount_applied": True,

            "discount_percent": 10,

            "final_price": final_price

            }

        

    else:

        return {

            "order_id": order_id,

            "total": total,

            "discount_applied": False,

            "final_price": total

            }




