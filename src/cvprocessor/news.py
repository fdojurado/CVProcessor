import pandas as pd


class NewsData:
    def __init__(self, pd_dataframe):
        self._pd_dataframe = pd_dataframe
        self._title = None
        self._date = None
        self._description = None
        self._pdf = None
        self._preprint = None
        self._code = None
        self._doi = None
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

    @property
    def pdf(self):
        return self._pdf

    @property
    def preprint(self):
        return self._preprint

    @property
    def code(self):
        return self._code

    @property
    def doi(self):
        return self._doi

    def _load_news(self):
        self._title = self._pd_dataframe["Title"]
        self._date = self._pd_dataframe["Date"]
        self._date = self._date.strftime("%b %d, %Y")
        self._description = self._pd_dataframe["Description"]
        self._pdf = self._pd_dataframe["PDF"]
        self._preprint = self._pd_dataframe["Preprint"]
        self._code = self._pd_dataframe["Code"]
        self._doi = self._pd_dataframe["DOI"]

    def __str__(self) -> str:
        string = f"Title: {self.title}\n"
        string += f"Date: {self.date}\n"
        string += f"Description: {self.description}\n"
        string += f"PDF: {self.pdf}\n"
        string += f"Preprint: {self.preprint}\n"
        string += f"Code: {self.code}\n"
        string += f"DOI: {self.doi}\n\n"
        return string

    def __repr__(self) -> str:
        string = f"NewsData(title={self.title}, date={self.date}, description={self.description}, pdf={self.pdf}, preprint={self.preprint}, code={self.code}, doi={self.doi})"
        return string


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

    def __str__(self):
        string = ""
        for news in self.news:
            string += str(news)
        return string

    def __repr__(self):
        repr = f"News(filename={self.filename}, news={self.news})\n"
        return repr
