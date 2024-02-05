from .my_types import NewsItem


def gather_news_items() -> list[NewsItem]:
    # Gather news items from different sources
    sources = [
        Twitter(),
        Reddit(),
        Arxiv(),
        NYTimes(),
        WashingtonPost(),
        Discord(),
        Medium(),
        Google(),
    ]
    news_items = [
        source.gather_news_items()
        for source in sources
    ]
    return news_items