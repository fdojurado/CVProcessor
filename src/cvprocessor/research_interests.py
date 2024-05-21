"""
This module contains the ResearchInterests class which is used to store
the research interests and keywords of a person.
"""
import pandas as pd


class ResearchInterests:
    """
    The ResearchInterests class is used to store the research interests and keywords of a person.

    Attributes:
    research_interests (str): The research interests of the person.
    keywords (list): The keywords related to the research interests.
    """

    def __init__(self):
        self.research_interests = str()
        self.keywords = []

    def get_interests(self) -> str:
        """
        Get the research interests of the person.
        """
        return self.research_interests

    def get_keywords(self) -> list:
        """
        Get the keywords related to the research interests.
        """
        return self.keywords

    def load(self, filename) -> None:
        """
        Load the research interests and keywords from the given file.
        """
        research_interests_pd = pd.read_excel(
            filename, sheet_name="Research_Interests")
        self.research_interests = research_interests_pd["Interests"].values[0]
        keywords = research_interests_pd["Keywords"]
        for keyword in keywords:
            self.keywords.append(keyword)

    def __repr__(self):
        string = (
            f"ResearchInterests("
            f"research_interests={self.research_interests}, "
            f"keywords={self.keywords})"
        )
        return string
