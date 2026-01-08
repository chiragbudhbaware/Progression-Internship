from fastapi import FastAPI

from routers import order, user,product,book

 

app = FastAPI()

 

@app.get("/")

def root():

    return {"message": "Hello World!"}

 

@app.get("/home")

def home():

    return {"message": "Welcome to home!"}

 

app.include_router(order.router)

app.include_router(product.router)

app.include_router(user.router)

app.include_router(book.router)




