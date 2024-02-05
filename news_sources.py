from .my_types import NewsSource


class Twitter(NewsSource):
    source_name="Twitter"
    last_retrieval=None

    def login(self, login_info: dict) -> bool:
        # Add code to login to Twitter using login_info
        return True

    def gather_news_items(self) -> list[NewsItem]:
        # Add code to read the top 300 tweets in the user's timeline or until the first tweet already seen
        tweets = api.get_user_timeline(count=300)
        news_items = [NewsItem(
            title=tweet.text,
            str_content=tweet.text,
            author=tweet.user.screen_name,
            publication_date=tweet.created_at,
            url=f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id_str}"
        ) for tweet in tweets]
        return news_items