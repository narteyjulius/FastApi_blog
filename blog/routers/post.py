from fastapi import FastAPI, status, HTTPException, Response, Depends, APIRouter
from typing import List, Optional
from sqlalchemy.orm import Session
import models
from database import get_db


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/") 
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    print(posts)
    return posts
