from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")

def root():
    return {"message": "Hello World!"}  

@app.get("/orders/{order_id}")

def get_order_price(order_id: int, total:float, coupon:Optional[str] = None):

    if coupon:
        discount_percent = 10
        final_price = total - (total * discount_percent / 100)
        return{
            "order_id": order_id,
            "original_price": total,
            "coupon": coupon,
            "final_price": final_price
        }
    else:
        return{
            "order_id": order_id,
            "original_price": total,
            "discount_applied": False,
            "final_price": total
        }