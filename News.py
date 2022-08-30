import requests
from datetime import date

NEWS_API = "87d20ac742a04bbb9b8610f2e846c61c"
DRAMATIC_CHANGE_CODE = 100


class News:

    def __init__(self, ticker_symbol):
        self.ticker = ticker_symbol


    def get_news(self, number_of_articles, update_code: int) -> [str]:

        if update_code == DRAMATIC_CHANGE_CODE:
            sort_by = "popularity"
        else:
            sort_by = "relevancy"

        yesterday = date(date.today().year, date.today().month, date.today().day - 1)
        parameters = {
            "q": self.ticker,
            "from": yesterday,
            "sortBy": sort_by,
            "apiKey": NEWS_API
        }

        response = requests.get("https://newsapi.org/v2/everything", params=parameters)
        response.raise_for_status()
        data = response.json()

        articles = []

        for article_num in range (0,number_of_articles):
            source_name = data["articles"][article_num]["source"]["name"]
            author = data["articles"][article_num]["author"]
            title = data["articles"][article_num]["title"]
            content = data["articles"][article_num]["content"]
            url = data["articles"][article_num]["url"]

            try:
                article = f"Name: {source_name}\nAuthor: {author}\nTitle: {title}\nContent: {content}\n\nFull article: {url}"

            except KeyError:
                print("Article not found..")

            else:
                articles.append(article)

        return articles

