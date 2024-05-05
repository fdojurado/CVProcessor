import pandas as pd


class NewsData:
    def __init__(self, pd_dataframe):
        self._pd_dataframe = pd_dataframe
        self._title = None
        self._date = None
        self._description = None
        self._load_news()

    @property
    def title(self):
        return self._title

    @property
    def date(self):
        return self._date

    @property
    def description(self):
        return self._description

    def _load_news(self):
        self._title = self._pd_dataframe["Title"]
        self._date = self._pd_dataframe["Date"]
        self._date = self._date.strftime("%b %d, %Y")
        self._description = self._pd_dataframe["Description"]

    def print(self):
        print(f"Title: {self._title}")
        print(f"Date: {self._date}")
        print(f"Description: {self._description}")
        print("\n")


class News:
    def __init__(self, filename):
        self._filename = filename
        self._news = self._load_news()

    @property
    def filename(self):
        return self._filename

    @property
    def news(self):
        return self._news

    def _load_news(self):
        news_df = pd.read_excel(self._filename, sheet_name="News")
        return [NewsData(row) for index, row in news_df.iterrows()]

    def print(self):
        print(f"Printing news from {self.filename}...")
        for news in self.news:
            news.print()
