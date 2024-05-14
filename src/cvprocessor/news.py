"""
This module contains the classes to handle news data.
"""
import pandas as pd


class NewsResources:
    """
    The NewsResources class is used to store the resources for a news item.

    Attributes:
    pdf (str): The PDF link for the news item.
    preprint (str): The preprint link for the news item.
    code (str): The code link for the news item.
    doi (str): The DOI link for the news item.
    """

    def __init__(self):
        self.pdf = None
        self.preprint = None
        self.code = None
        self.doi = None

    def load(self, filename):
        """
        Load the resources for the news item.
        """
        self.pdf = filename["PDF"]
        self.preprint = filename["Preprint"]
        self.code = filename["Code"]
        self.doi = filename["DOI"]

    def __str__(self):
        string = f"PDF: {self.pdf}\n"
        string += f"Preprint: {self.preprint}\n"
        string += f"Code: {self.code}\n"
        string += f"DOI: {self.doi}\n"
        return string

    def __repr__(self):
        string = (
            f"NewsResources("
            f"pdf={self.pdf}, "
            f"preprint={self.preprint}, "
            f"code={self.code}, "
            f"doi={self.doi})"
        )
        return string


class NewsData:
    """
    The NewsData class is used to store the data for a news item.

    Attributes:
    title (str): The title of the news item.
    date (str): The date of the news item.
    description (str): The description of the news item.
    resources (NewsResources): The resources for the news item.
    """

    def __init__(self):
        self.title = str()
        self.date = str()
        self.description = str()
        self.resources = NewsResources()

    def load(self, pd_dataframe):
        """
        Load the news data from a Pandas DataFrame.
        """
        self.title = pd_dataframe["Title"]
        self.date = pd_dataframe["Date"]
        self.date = self.date.strftime("%b %d, %Y")
        self.description = pd_dataframe["Description"]
        self.resources.load(pd_dataframe)

    def __str__(self) -> str:
        string = f"Title: {self.title}\n"
        string += f"Date: {self.date}\n"
        string += f"Description: {self.description}\n"
        string += str(self.resources)
        return string

    def __repr__(self) -> str:
        string = (
            f"NewsData("
            f"title={self.title}, "
            f"date={self.date}, "
            f"description={self.description}, "
            f"resources={repr(self.resources)})"
        )
        return string


class News:
    """
    The News class is used to store the news data.

    Attributes:
    news (list): A list of NewsData objects.

    Methods:
    __init__(filename): Initializes the News class by loading the news data from the given file.
    __str__(): Returns a string representation of the News class.
    __repr__(): Returns a string representation of the News class.
    """

    def __init__(self):
        self.news = []

    def load(self, filename):
        news_df = pd.read_excel(filename, sheet_name="News")
        for _, row in news_df.iterrows():
            self.news.append(NewsData())
            self.news[-1].load(row)

    def __str__(self):
        string = ""
        for news in self.news:
            string += str(news) + "\n"
        return string

    def __repr__(self):
        string = f"News(news={repr(self.news)})\n"
        return string
