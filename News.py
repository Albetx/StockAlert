import requests
from datetime import date

NEWS_API = "87d20ac742a04bbb9b8610f2e846c61c"


class News:

    def __init__(self, ticker_symbol):
        self.ticker = ticker_symbol

    def get_news(self) -> [str]:

        yesterday = date(date.today().year, date.today().month, date.today().day - 1)
        parameters = {
            "q": self.ticker,
            "from": yesterday,
            "sortBy": "popularity",
            "apiKey": NEWS_API
        }

        response = requests.get("https://newsapi.org/v2/everything", params=parameters)
        response.raise_for_status()
        data = response.json()

        articles = []

        for article_num in range (0,3):
            source_name = data["articles"][article_num]["source"]["name"]
            author = data["articles"][article_num]["author"]
            title = data["articles"][article_num]["title"]
            description = data["articles"][article_num]["description"]
            content = data["articles"][article_num]["content"]
            url = data["articles"][article_num]["url"]

            try:
                article = f"Name: {source_name}\nAuthor: {author}\nTitle: {title}\n" \
                          f"Description: {description}\nContent: {content}\n\nFull article: {url}"

            except KeyError:
                print("Article not found..")

            else:
                articles.append(article)

        return articles

