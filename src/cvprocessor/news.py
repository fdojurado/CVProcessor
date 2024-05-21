"""
This module contains the classes to handle news data.
"""
import pandas as pd
from cvprocessor.links.links import Links


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
        self.links = Links()

    def get_title(self):
        """
        Get the title of the news item.
        """
        return self.title

    def get_date(self):
        """
        Get the date of the news item.
        """
        return self.date

    def get_description(self):
        """
        Get the description of the news item.
        """
        return self.description

    def load(self, pd_dataframe):
        """
        Load the news data from a Pandas DataFrame.
        """
        self.title = pd_dataframe["Title"]
        self.date = pd_dataframe["Date"]
        self.date = self.date.strftime("%b %d, %Y")
        self.description = pd_dataframe["Description"]
        self.links.load(pd_dataframe)

    def __repr__(self) -> str:
        string = (
            f"NewsData("
            f"title={self.title}, "
            f"date={self.date}, "
            f"description={self.description}, "
            f"links={repr(self.links)})"
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
        """
        Load the news data from the given file.
        """
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

    def __iter__(self):
        return iter(self.news)
