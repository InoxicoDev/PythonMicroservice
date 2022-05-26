# more details: https://www.tutorialsbuddy.com/python-fastapi-bigger-applications-multiple-separate-files

from uuid import uuid4
from fastapi import APIRouter
from fastapi import Query
from typing import Optional

from src.models.book import Book
from src.services.book_service import BookService

service = BookService()

#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/books",
    tags=["Book"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_root():
    return service.get_all_books()

@router.get("/{book_id}")
async def read_book(book_id: int):
    return service.get_book(book_id)

