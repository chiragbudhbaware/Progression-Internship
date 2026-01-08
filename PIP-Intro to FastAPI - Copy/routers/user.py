from fastapi import APIRouter

from typing import Optional

 

router = APIRouter(

    prefix="/user",

    tags=["users"]

)

 

@router.get("/all")  # Static route

def get_all_users():

    return {"message": "All users"}

 

@router.get("/{username}")

def get_user(username:str):

    return {"message": f"User profile for {username}"}

 

@router.get("/{username}/post/{post_id}")

def get_post(username:str, post_id: int):

    return {"message": f"Post {post_id} by user {username}"}




