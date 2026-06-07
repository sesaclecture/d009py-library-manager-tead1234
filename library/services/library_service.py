
from __future__ import annotations
from typing import Iterable, List
from library.models.book import Book
from library.services.base_service import BaseService


class LibraryService(BaseService):
    """도서 목록을 메모리에서 관리하는 서비스.
    TODO:
      - 내부 상태를 캡슐화하기 위해 _books(list[Book])를 사용
      - add_book/remove_book/list_books/find_book 구현
      - 존재하지 않는 책 삭제/검색 시 ValueError 발생
        """
    
    def __init__(self) -> None:
        self._books = dict()

    def add_book(self, book: Book) -> None:
        self._books[book.title] = book

    def remove_book(self, title: str) -> None:
        if title in self._books:
            del self._books[title]
        else:
            raise ValueError

    def list_books(self) -> Iterable[Book]:
        return [Book(v.title, v.author, v.year) for v in self._books.values()]

    def find_book(self, title: str) -> Book:
       
       if title in self._books:
           return self._books[title]
       else: 
           raise ValueError
