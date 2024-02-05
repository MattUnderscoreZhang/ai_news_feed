from .news_items import gather_news_items
from .news_summary import group_and_summarize


def main():
    news_items = gather_news_items()
    grouped_news = group_and_summarize(news_items)
    print(grouped_news)