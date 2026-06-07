
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any ,ClassVar  


@dataclass
class Book:
    """책 정보를 표현하는 데이터 클래스.
    TODO: 아래 요구사항을 만족하도록 구현을 보완하세요.
    - 인스턴스 변수: title(str), author(str), year(int)
    - 클래스 변수: book_count(int) — 생성될 때마다 +1
    - __str__는 "{title} by {author} ({year})" 형식 반환
    - @classmethod from_dict(cls, data: Dict[str, Any]) -> Book 구현
    """
    title: str
    author: str
    year: int
    book_count: ClassVar[int] = 0 
  
    def __post_init__(self):
        Book.book_count += 1
        

    def __str__(self) -> str:
        
        return f"{self.title} by {self.author} ({self.year})"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Book":
        # TODO: dict에서 title/author/year를 읽어 Book 생성
        return cls(
            title=data.get("title", ""),
        author=data.get("author", ""),
        year=data.get("year", 0)
        )
