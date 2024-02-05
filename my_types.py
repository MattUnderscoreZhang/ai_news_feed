from dataclasses import dataclass
from datetime import datetime


@dataclass
class NewsItem:
    title: str
    str_content: str
    author: str
    publication_date: datetime
    url: str


@dataclass
class NewsSource:
    source_name: str
    last_retrieval: datetime | None

    def login(self, login_info: dict) -> bool:
        pass

    def gather_news_items(self) -> list[NewsItem]:
        pass